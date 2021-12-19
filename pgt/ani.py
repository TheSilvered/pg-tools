"""
pgt.ani

Type: module

Description: module that contains the classes that define how animations
    work

Constants:
    - PERC
    - PREV_VAL
    - STARTING_VAL
    - FRAME
    - ANIMATION

Abstract classes:
    - FuncAniFrames
    - AniBase
    - FuncAniBase

Classes:
    - TextureAni
    - PosAni
    - TextAni

To make a custom animation you need to:

# make a class that inherits from pgt.AniBase (if the animation should
# only support a list of frames) or from pgt.FuncAniBase (if the
# animation can get its value from a function)
class MyAnimation(pgt.AniBase):

    # in the start method add a statement to save the initial value of
    # the property the animation changes.
    def start(self, *args, **kwargs):
        super().start(*args, **kwargs)
        self.element_val = self.e.[ELEMENT_PROPERTY]

    def set_element(self):
        # here goes any operation that the animation should do when
        # a frame passes
        # you can use self.get_frame() to get the value of the current
        # frame, returned either by the function or the list of frames
        pass

    def reset_element(self):
        # here goes any operation that the animation should do when
        # the animation restores the initial value of the element
        pass


Here is the code of PosAni:

class PosAni(FuncAniBase):
    def start(self, *args, **kwargs):
        super().start(*args, **kwargs)
        # it copies the position else an alias would form
        self.element_val = self.e.pos.copy()

    def set_element(self):
        # it assumes that get_frame() always returns a valid position
        self.e.pos = self.get_frame()

    def reset_element(self):
        self.e.pos = self.element_val
"""

from abc import ABC, abstractmethod
import time as t
from typing import Callable, Optional, Sized, Any
from .element import AniElement

PERC         = 0b00001
PREV_VAL     = 0b00010
STARTING_VAL = 0b00100
FRAME        = 0b01000
ANIMATION    = 0b10000


class FuncAniFrames:
    """
    FuncAniFrames

    Type: class

    Description: class used by subclasses of FuncAniBase to define
        frames that use a function and not a list

    Args:
        'function' (lambda, function): a function or lambda that returns
            a value that can later be used by the animation class
        'frames' (int): the total number of frames of the animation

    Attrs:
        '_func' (function): see 'function' in arguments
        '_frames' (int): see 'frames' in arguments

    Magic methods:
        '__len__()' (int): returns the total number of frames

    See tests/animations.PosAni.py for examples
    """
    def __init__(self, function: Callable, frames: int):
        self._func = function
        self._frames = frames

    def __len__(self):
        return self._frames


class AniBase(ABC):
    """
    AniBase(ABC)

    Type: abstract class

    Description: base to create an animation that can be used by
        an instance of pgt.element.AniElement

    Args:
        'name' (str): the name of the animation, it will be set as an
            attribute of the element that refers to this animation
        'element' (pgt.element.AniElement): the element to which the
            animation is assigned, defaults to None and should not be
            set manually, to set it use the pgt.element.AniElement.add_ani
            method to add the animation to an element
        'id_' (int): defaults to None, if set any animation running with
            the same id will be stopped upon calling the 'start' or
            'restart' methods
        'frames' (iterable): an iterable containing each frame of the
            animation
        'time' (float): the time that should elapse between frames
        'tot_time' (float): the time that should pass between the first
            and last frame, overwrites 'time' if set
        'loop' (bool): if the animation should restart after the last
            frame
        'reset_on_end' (bool): if at the end of the animation the
            starting value of the animation should be restored

    Attrs:
        'name' (str): see 'name' in arguments
        'id' (int): see 'id_' in arguments
        'frames' (iterable): see 'frames' in arguments
        'element_val' (Any): used to store the starting state of the
            animation to restore the original value
        '_loop' (bool): see 'loop' in arguments
        '_current_frame' (int): the index of the frame currently
            displayed by the animation, if the animation was stopped
            or has ended, returns the index of the last shown frame
        '_tot_frames' (int): the total number of frames of the animation
        '_last_frame' (float): the time that the last frame was shown
        '_ending' (bool): if the animation is going to stop before showing
            the next frame
        '_AniBase__running': if the animation is currently playing
        '_start_time' (float): when the animation started
        'e' (AniElement): the element of the animation
        '_reset_on_end' (bool): see 'reset_on_end' in arguments
        '_time' (float): see 'time' in arguments, if 'tot_time' is set
            '_time' will be automatically set

    Methods:
        'start(frame=0, start_time=None)' (None): starts the animation.
            'frame' (int): the frame the animation should be started at
            'start_time' (float): when the animation should start, if
                None, defaults to the current system time
        'update(frame_time)' (None): updates the frame of the animation,
            is usually called automatically by AniElement.update_ani()
            'frame_time' (float): value that marks the current time for
                the animation, AniElement.update_ani() sets it to be
                the current time
        'stop()' (None): starts the stopping process of the animation,
            note that the animation stops only at the end of the current
            frame
        'force_stop()' (None): stops immediately the animation
        'restart(*args, **kwargs)' (None): restarts the animation, if
            it's not running acts like 'start'
        'get_frame()' (Any): returns the current frame; not the attribute,
            the actual value in 'frames'
        'set_frames(frames)' (None): sets a new list of frames for the
            animation
            'frames' (iterable): the new set of frames

    Magic methods:
        '__len__()' (int): returns the total length of the animation in
            seconds

    Abstract methods:
        'set_element()' (None): changes the element according to the
            current frame (e.g. TextureAni changes the image)
        'reset_element()' (None): called only if 'reset_on_end' is true,
            resets the element to be like when the animation started
            (e.g. PosAni resets the element's position)
    """
    def __init__(self,
       name: Optional[str] = None,
       element: Optional[AniElement] = None,
       id_: Optional[int] = None,
       frames: Sized = None,
       time: float = 0.001,
       tot_time: float = 0.0,
       loop: bool = False,
       reset_on_end: bool = True):

        if element is not None: setattr(element, name, self)

        self.name = name
        self.id = id_
        self.frames = frames
        self.element_val = None
        self._loop = loop
        self._current_frame = 0
        self._tot_frames = len(frames)
        self._last_frame = 0
        self._ending = False
        self.__running = False
        self._start_time = 0
        self.e = element
        self._reset_on_end = reset_on_end
        if tot_time != 0:
            self._time = tot_time / self._tot_frames
        else:
            self._time = time

    def __str__(self):
        return_string = f"name: {self.name}, frames: {self._tot_frames}"
        if self.id: return_string += f", id: {self.id}"
        return return_string

    def __repr__(self):
        return str(self)

    def start(self, frame: int = 0, start_time: Optional[float] = None):
        if self._ending:
            self._ending = False
            return
        if self.__running:
            return
        if not start_time: start_time = t.time()
        self._start_time = start_time
        self._last_frame = start_time
        self._current_frame = frame
        if self.id is None:
            self.e.current_ani.append((self.name, self.id))
        else:
            try:
                # overrides any animation with the same id
                ids = tuple(map(lambda x: x[1], self.e.current_ani))
                name = self.e.current_ani[ids.index(self.id)][0]
                getattr(self.e, name).force_stop()
                self.e.current_ani.append((self.name, self.id))
            except ValueError:
                self.e.current_ani.append((self.name, self.id))
        self.__running = True

    def update(self, frame_time: float):
        elapsed_time = frame_time - self._last_frame

        if elapsed_time < self._time: return

        if self._ending:
            self.force_stop()
            return

        try:
            self._current_frame += int(elapsed_time // self._time)
        except ZeroDivisionError:
            self._current_frame += 1

        if self._loop:
            if self._current_frame >= self._tot_frames:
                self._start_time += self._time * self._tot_frames
            self._current_frame %= self._tot_frames
        elif self._current_frame >= self._tot_frames:
            self.force_stop()

        self._last_frame = self._start_time + self._time * self._current_frame

    def stop(self):
        self._ending = True

    def force_stop(self):
        if not self.__running: return
        self._ending = False
        self.e.current_ani.remove((self.name, self.id))
        self.__running = False
        if self._reset_on_end:
            self.reset_element()

    def restart(self, *args, **kwargs):
        if not self.__running:
            self.start(*args, **kwargs)
            return

        self._start_time = t.time()
        self._last_frame = t.time()
        self._current_frame = 0
        self._ending = False
        self.__running = True
        if self._reset_on_end:
            self.reset_element()

    def get_frame(self):
        return self.frames[self._current_frame]

    def set_frames(self, frames: Sized):
        self._tot_frames = len(frames)
        self.frames = frames

    def __len__(self):
        return self._time * self._tot_frames

    @abstractmethod
    def set_element(self):
        pass

    @abstractmethod
    def reset_element(self):
        pass


class FuncAniBase(AniBase):
    """
    FuncAniBase(AniBase)

    Type: abstract class

    Description: base to create an animation that can use a function to
        get the value of the frame

    Args:
        'starting_val' (Any): a value that specifies the starting point
            of the animation, is never changed
        'func_args' (int): what arguments should be passed to the
            function, these are:
            - pgt.ani.PERC: the percentage of the animation (from 0 to 1)
            - pgt.ani.PREV_VAL: the previous value returned by the
                function, if starting val is not set, the first time
                'element_val' is passed
            - pgt.ani.STARTING_VAL: 'start_val' in the arguments
            - pgt.ani.FRAME: the number of the current frame
            - pgt.ani.ANIMATION: the animation object itself

    Attrs:
        '__using_func' (bool): if the animation is using a function or
            a list of frames predefined
        '__pending' (int): how many times the function should be called
            to keep up with the expected frame
        'starting_val' (Any): see 'starting_val' in arguments
        '__prev_val' (Any): the previous value returned by the function
        '__func_args' (int): see 'func_args' in arguments
    """
    def __init__(self,
       starting_val: Any = None,
       func_args: int = PREV_VAL,
       *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__using_func = isinstance(self.frames, FuncAniFrames)
        self.__pending = 0
        self.starting_val = starting_val
        self.__prev_val = starting_val
        self.__func_args = func_args

    def start(self, starting_val: Any = None, frame: int = 0, start_time: Optional[float] = None):
        if starting_val is None: self.__prev_val = self.starting_val
        else: self.__prev_val = starting_val
        super().start(frame, start_time)

    def update(self, frame_time):
        if not self.__using_func:
            super().update(frame_time)
            return

        elapsed_time = frame_time - self._last_frame

        if elapsed_time < self._time: return

        if self._ending:
            self.force_stop()
            return

        try:
            self.__pending = int(elapsed_time // self._time)
        except ZeroDivisionError:
            self.__pending += 1

        self._current_frame += self.__pending

        if self._loop:
            if self._current_frame > self._tot_frames:
                self._start_time += self._time * self._tot_frames
            self._current_frame %= self._tot_frames
        elif self._current_frame > self._tot_frames:
            self.__pending -= self._current_frame % self._tot_frames
            self._current_frame = self._tot_frames
            self._ending = True

        self._last_frame = self._start_time + self._time * self._current_frame

    def restart(self, *args, **kwargs):
        super().restart(*args, **kwargs)
        self.__pending = 0

    @property
    def get_frame(self):
        if not self.__using_func: return self.frames[self._current_frame]
        return_val = self.__prev_val
        if return_val is None and self.__pending == 0: return self.element_val
        for i in range(self.__pending):
            frame = self._current_frame - (self.__pending - i) + 1
            perc = frame / self._tot_frames
            args = []
            if self.__func_args & PERC: args.append(perc)
            if self.__func_args & PREV_VAL: args.append(return_val)
            if self.__func_args & STARTING_VAL: args.append(self.starting_val)
            if self.__func_args & FRAME: args.append(frame)
            if self.__func_args & ANIMATION: args.append(self)
            return_val = self.frames._func(*args)
        self.__pending = 0
        self.__prev_val = return_val
        return return_val

    @abstractmethod
    def set_element(self):
        pass

    @abstractmethod
    def reset_element(self):
        pass


class TextureAni(AniBase):
    """
    TextureAni(AniBase)

    Type: class

    Description: animation that changes the texture of the element
    """
    def start(self, *args, **kwargs):
        super().start(*args, **kwargs)
        self.element_val = self.e.image

    def set_element(self):
        self.e.change_image(self.get_frame())

    def reset_element(self):
        self.e.image = self.element_val


class PosAni(FuncAniBase):
    """
    TextureAni(FuncAniBase)

    Type: class

    Description: animation that changes the position of the element
    """
    def start(self, *args, **kwargs):
        super().start(*args, **kwargs)
        self.element_val = self.e.pos.copy()

    def set_element(self):
        self.e.pos = self.get_frame

    def reset_element(self):
        self.e.pos = self.element_val


class TextAni(AniBase):
    """
    TextureAni(AniBase)

    Type: class

    Description: animation that changes the text of a label
    """
    def start(self, *args, **kwargs):
        super().start(*args, **kwargs)
        self.element_val = self.e.text

    def set_element(self):
        self.e.text = self.get_frame()

    def reset_element(self):
        self.e.text = self.element_val


class RotAni(FuncAniBase):
    """
    TextureAni(FuncAniBase)

    Type: class

    Description: animation that changes the rotation of the element
    """
    def start(self, *args, **kwargs):
        super().start(*args, **kwargs)
        self.element_val = self.e._rot

    def set_element(self):
        self.e.rotate(self.get_frame, True)

    def reset_element(self):
        self.e.rotate(self.element_val, True)


class ScaleAni(FuncAniBase):
    """
    TextureAni(FuncAniBase)

    Type: class

    Description: animation that scales the element

    Args:
        'smooth' (bool): if the animation should use 
        pygame.transform.smoothscale instead of pygame.transform.scale

    Attrs:
        'smooth': see 'smooth' in args
    """
    def __init__(self, smooth: bool = False, *args, **kwargs):
        self.smooth = smooth
        super().__init__(*args, **kwargs)

    def start(self, *args, **kwargs):
        super().start(*args, **kwargs)
        self.element_val = self.e.size

    def set_element(self):
        self.e.scale(self.get_frame, self.smooth)

    def reset_element(self):
        self.e.scale(self.element_val)
