from .mathf import clamp
from .type_hints import _col_type
from typing import List
from numbers import Real


def add_col(col1: _col_type, col2: _col_type) -> List[int]:
    return [clamp(c1 + c2, 0, 255) for c1, c2 in zip(col1, col2)]


def sub_col(col1: _col_type, col2: _col_type) -> List[int]:
    return [clamp(c1 - c2, 0, 255) for c1, c2 in zip(col1, col2)]


def mul_col(col1: _col_type, col2: _col_type) -> List[int]:
    return [clamp(c1 * c2, 0, 255) for c1, c2 in zip(col1, col2)]


def min_col(col1: _col_type, col2: _col_type) -> List[int]:
    return [min(c1, c2) for c1, c2 in zip(col1, col2)]


def max_col(col1: _col_type, col2: _col_type) -> List[int]:
    return [max(c1, c2) for c1, c2 in zip(col1, col2)]


def calc_alpha(new_color: _col_type, prev_color: _col_type, alpha: Real) -> List[int]:
    return [alpha * c1 + (1 - alpha) * c2 for c1, c2 in zip(new_color, prev_color)]


BLACK       = (1  , 1  , 1  , 255)
WHITE       = (255, 255, 255, 255)

RED         = (255, 0  , 0  , 255)
GREEN       = (0  , 255, 0  , 255)
BLUE        = (0  , 0  , 255, 255)
YELLOW      = (255, 255, 0  , 255)
CYAN        = (0  , 255, 255, 255)
MAGENTA     = (255, 0  , 255, 255)

MAROON      = (127, 0  , 0  , 255)
EMERALD     = (0  , 127, 0  , 255)
NAVY        = (0  , 0  , 127, 255)
OLIVE       = (127, 127, 0  , 255)
TEAL        = (0  , 127, 127, 255)
PURPURA     = (127, 0  , 127, 255)

ORANGE      = (255, 127, 0  , 255)
LIME        = (127, 255, 0  , 255)
AQUA        = (0  , 255, 127, 255)
LIGHT_BLUE  = (0  , 127, 255, 255)
PURPLE      = (127, 0  , 255, 255)
FUCHSIA     = (255, 0  , 127, 255)

SALMON      = (255, 127, 127, 255)
LIGHT_GREEN = (127, 255, 127, 255)
COBALT      = (127, 127, 255, 255)

LEMON       = (255, 255, 127, 255)
SKY_BLUE    = (127, 255, 255, 255)
PINK        = (255, 127, 255, 255)


GRAY = lambda c: (clamp(c, 0, 255), clamp(c, 0, 255), clamp(c, 0, 255))

R = lambda c: (clamp(c, 0, 255), 0, 0)

G = lambda c: (0, clamp(c, 0, 255), 0)

B = lambda c: (0, 0, clamp(c, 0, 255))
