#!/usr/bin/env python3

import json
from math import sin as _sin, cos as _cos, radians as _rad
from os import PathLike
from typing import Optional, Union

from pygame import Surface, PixelArray
from pygame.image import load as _load

from .ani import TextureAni
from .mathf import Size, Pos
from .type_hints import _col_type, _size


def parse_json_file(path: Union[str, PathLike],
                    encoding: str = "utf-8") -> Union[list, dict]:
    """
    parse_json_file(path, encoding='utf-8')

    Type: function

    Description: given a path, it opens the file, parses the data and
        returns it

    Args:
        'path' (str, os.PathLike): the path of the file
        'encoding' (str): default UTF-8, encoding used to open the file
    """
    with open(path, encoding=encoding) as f:
        data = json.load(f)
    return data


def load_image(path: Union[str, PathLike],
               has_alpha: bool = False,
               surface: Optional[Surface] = None) -> Surface:
    """
    load_image(path, has_alpha=False, surface=None)

    Type: function

    Description: loads an image converting it

    Args:
        'path' (str, os.PathLike): the path of the image file
        'has_alpha' (bool): if the alpha values of the image should be
            kept
        'surface' (Surface): the surface where the image will be blit,
            defaults to the window, only works with alpha values
    """
    if has_alpha:
        if surface: return _load(path).convert_alpha(surface)
        return _load(path).convert_alpha()
    else:
        return _load(path).convert()


def filled_surface(size: _size, color: _col_type, flags: int = 0) -> Surface:
    """
    filled_surface(size, color, flags=0)

    Type: function

    Description: returns a new surface filled with the specified color

    Args:
        'size' (Sequence): the size of the surface
        'color' (pygame.Color): the color of the surface
        'flags' (int): additional flags for the surface
    """
    surf = Surface(Size(size), flags)
    surf.fill(color)
    return surf.convert()


def replace_color(surface: Surface, col1: _col_type, col2: _col_type) -> Surface:
    """
    replace_color(surface, col1, col2)

    Type: function

    Description: creates a new surface replacing one color from the old one

    Args:
        'surface' (pygame.Surface): the original surface
        'col1' (pygame.Color): the color to replace
        'col2' (pygame.Color): the color that replaces the old one
    """
    pixel_arr = PixelArray(surface.copy())
    pixel_arr.replace(col1, col2)
    new_img = pixel_arr.surface.copy()
    new_img.unlock()
    return new_img


def change_image_ani(image: Surface,
                     name: Optional[str] = None,
                     id_: Optional[int] = None) -> TextureAni:
    """
    change_image_ani(image, name=None, id_None)

    Type: function

    Description: returns a TextureAni that simply changes the image of
        an AniElement

    Args:
        'image' (pygame.Surface): the image to change the element to
        'name' (str?): the name of the animation, defaults to None
        'id_' (int?): the ID of the animation, defaults to None

    Return type: TextureAni
    """
    return TextureAni(
        name=name,
        frames=[image],
        time=0,
        id_=id_,
        reset_on_end=False
    )


def transform_func(element):
    """
    transform_func(element)

    Type: function

    Description: this function returns another function that transforms
        any screen coordinates to coordinates relative to an element
        (including the rotation). This may be useful as a
        'transform_mouse_pos' function for a MouseInteractionElement
        that is part of a SurfaceElement.

    Args:
        'element' (Element): the element of reference

    Return type: function
    """
    def func(x):
        x = Pos(x)

        if element._rot == 0:
            return x - element.ul

        s = _sin(_rad(element._rot))
        c = _cos(_rad(element._rot))

        p = x - element.cc

        p = Pos(p.x * c - p.y * s,
                p.x * s + p.y * c)

        return element._size / 2 + p

    return func
