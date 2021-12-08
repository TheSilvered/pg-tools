"""
pgt.pos_size

Type: module

Description: module that defines classes to work easily with positions
    and sizes

Classes:
    - Pos
    - Size
"""


class Pos:
    """
    Pos

    Type: class

    Description: a class that simplifies working with coordinates

    Initialisation: you can give two separate arguments or an iterable
        containing them, and they will be automatically be set

    Attrs:
        'x' (Any): position on the x-axis
        'y' (Any): position on the y-axis

    Methods:
        'list()' (list): converts the position into a list
        'tuple()' (tuple): converts the position into a tuple
        'int()' (Pos): makes integers x and y
        'copy()' (Pos): returns a copy of itself

    How operations work: if given an iterable with size 2 (Pos is an
        iterable) it will make the operation between x and the first
        object, and between y and the second object, else just adds
        the object to both x and y.
        >>> Pos(2, 3) + [10, 5] == Pos(12, 8)

        >>> Pos(4, 4) - 3 == Pos(1, 1)

        # Pos can contain any type of object
        >>> Pos((1,), (2,)) + (1, 2) == Pos((1, 1, 2), (2, 1, 2))

    """
    __slots__ = "x", "y"

    def __init__(self, *args):
        try:
            x, y = args
        except (TypeError, ValueError):
            try:
                x, y = args[0]
            except (TypeError, ValueError):
                y = x = args[0]

        self.x = x
        self.y = y

    def __repr__(self):
        return f"Pos({self.x}, {self.y})"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        try:
            x = self.x + other[0]
            y = self.y + other[1]
        except (TypeError, ValueError):
            x = self.x + other
            y = self.y + other
        return self.c(x, y)

    def __sub__(self, other):
        try:
            x = self.x - other[0]
            y = self.y - other[1]
        except (TypeError, ValueError):
            x = self.x - other
            y = self.y - other
        return self.c(x, y)

    def __mul__(self, other):
        try:
            x = self.x * other[0]
            y = self.y * other[1]
        except (TypeError, ValueError):
            x = self.x * other
            y = self.y * other
        return self.c(x, y)

    def __truediv__(self, other):
        try:
            x = self.x / other[0]
            y = self.y / other[1]
        except (TypeError, ValueError):
            x = self.x / other
            y = self.y / other
        return self.c(x, y)

    def __floordiv__(self, other):
        try:
            x = self.x // other[0]
            y = self.y // other[1]
        except (TypeError, ValueError):
            x = self.x // other
            y = self.y // other
        return self.c(x, y)

    def __mod__(self, other):
        try:
            x = self.x % other[0]
            y = self.y % other[1]
        except (TypeError, ValueError):
            x = self.x % other
            y = self.y % other
        return self.c(x, y)

    def __pow__(self, other):
        try:
            x = self.x ** other[0]
            y = self.y ** other[1]
        except (TypeError, ValueError):
            x = self.x ** other
            y = self.y ** other
        return self.c(x, y)

    def __lshift__(self, other):
        try:
            x = self.x << other[0]
            y = self.y << other[1]
        except (TypeError, ValueError):
            x = self.x << other
            y = self.y << other
        return self.c(x, y)

    def __lshift__(self, other):
        try:
            x = self.x >> other[0]
            y = self.y >> other[1]
        except (TypeError, ValueError):
            x = self.x >> other
            y = self.y >> other
        return self.c(x, y)

    def __and__(self, other):
        try:
            x = self.x & other[0]
            y = self.y & other[1]
        except (TypeError, ValueError):
            x = self.x & other
            y = self.y & other
        return self.c(x, y)

    def __or__(self, other):
        try:
            x = self.x | other[0]
            y = self.y | other[1]
        except (TypeError, ValueError):
            x = self.x | other
            y = self.y | other
        return self.c(x, y)

    def __xor__(self, other):
        try:
            x = self.x ^ other[0]
            y = self.y ^ other[1]
        except (TypeError, ValueError):
            x = self.x ^ other
            y = self.y ^ other
        return self.c(x, y)

    def __invert__(self):
        return self.c(~self.x, ~self.y)

    def __round__(self, ndigits=None):
        return self.c(round(self.x, ndigits), round(self.y, ndigits))

    def __abs__(self):
        return self.c(abs(self.x), abs(self.y))

    def __neg__(self): return self.c(-self.x, -self.y)

    def __floor__(self): return self.c(self.x.__floor__(), self.y.__floor__())

    def __ceil__(self): return self.c(self.x.__ceil__(), self.y.__ceil__())

    def __trunc__(self, ndigits):
        return self.c(self.x.__trunc__(ndigits), self.y.__trunc__(ndigits))

    def __radd__(self, other): return self.__add__(other)

    def __rsub__(self, other): return -self.__sub__(-other)

    def __rmul__(self, other): return self.__mul__(other)

    def __rand__(self, other): return self.__and__(other)

    def __ror__(self, other): return self.__or__(other)

    def __rxor__(self, other): return self.__xor__(other)

    def __getitem__(self, i):
        if i == 0: return self.x
        elif i == 1: return self.y
        else: raise IndexError(f"index {i} out of range for size 2")

    def __setitem__(self, i, value):
        if i == 0: self.x = value
        elif i == 1: self.y = value
        else: raise IndexError(f"index {i} out of range for size 2")

    def __len__(self): return 2

    def __eq__(self, other):
        return self.x == other[0] and self.y == other[1]

    def __ne__(self, other):
        return self.x != other[0] or self.y != other[1]

    def __gt__(self, other):
        return self.x > other[0] and self.y > other[1]

    def __lt__(self, other):
        return self.x < other[0] and self.y < other[1]

    def __ge__(self, other):
        return self == other or self > other

    def __le__(self, other):
        return self == other or self < other

    def list(self):
        return [self.x, self.y]

    def tuple(self):
        return self.x, self.y

    def int(self):
        return self.c(int(self.x), int(self.y))

    def copy(self):
        return self.c(self.x, self.y)

    @classmethod
    def c(cls, *args):
        return cls(*args)


class Size(Pos):
    """
    Size

    Type: class

    Description: it's the same as Pos and adds two attributes

    Attrs:
        'w' (Any): width, the same as 'x'
        'h' (Any): width, the same as 'y'
    """
    @property
    def w(self): return self.x
    @w.setter
    def w(self, value): self.x = value

    @property
    def h(self): return self.y
    @h.setter
    def h(self, value): self.y = value

    def __repr__(self):
        return f"Size({self.w}, {self.h})"
