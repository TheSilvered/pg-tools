from .mathf import clamp


def add_col(col1, col2):
    return [clamp(c1 + c2, 0, 255) for c1, c2 in zip(col1, col2)]


def sub_col(col1, col2):
    return [clamp(c1 - c2, 0, 255) for c1, c2 in zip(col1, col2)]


def mul_col(col1, col2):
    return [clamp(c1 * c2, 0, 255) for c1, c2 in zip(col1, col2)]


def min_col(col1, col2):
    return [min(c1, c2) for c1, c2 in zip(col1, col2)]


def max_col(col1, col2):
    return [max(c1, c2) for c1, c2 in zip(col1, col2)]


def calc_alpha(new_color, prev_color, alpha):
    return alpha * new_color[0] + (1 - alpha) * prev_color[0],\
           alpha * new_color[1] + (1 - alpha) * prev_color[1],\
           alpha * new_color[2] + (1 - alpha) * prev_color[2]


BLACK       = (1  , 1  , 1  )
WHITE       = (255, 255, 255)

RED         = (255, 0  , 0  )
GREEN       = (0  , 255, 0  )
BLUE        = (0  , 0  , 255)
YELLOW      = (255, 255, 0  )
CYAN        = (0  , 255, 255)
MAGENTA     = (255, 0  , 255)

MAROON      = (127, 0  , 0  )
EMERALD     = (0  , 127, 0  )
NAVY        = (0  , 0  , 127)
OLIVE       = (127, 127, 0  )
TEAL        = (0  , 127, 127)
PURPURA     = (127, 0  , 127)

ORANGE      = (255, 127, 0  )
LIME        = (127, 255, 0  )
AQUA        = (0  , 255, 127)
LIGHT_BLUE  = (0  , 127, 255)
PURPLE      = (127, 0  , 255)
FUCHSIA     = (255, 0  , 127)

SALMON      = (255, 127, 127)
LIGHT_GREEN = (127, 255, 127)
COBALT      = (127, 127, 255)

LEMON       = (255, 255, 127)
SKY_BLUE    = (127, 255, 255)
PINK        = (255, 127, 255)


GRAY = lambda c: (clamp(c, 0, 255), clamp(c, 0, 255), clamp(c, 0, 255))

R = lambda c: (clamp(c, 0, 255), 0, 0)

G = lambda c: (0, clamp(c, 0, 255), 0)

B = lambda c: (0, 0, clamp(c, 0, 255))
