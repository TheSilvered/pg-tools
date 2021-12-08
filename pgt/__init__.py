"""
Pygame Tools by TheSilvered
This package requires pygame

Classes:
    - Pos  (pgt.pos_size.Pos)
    - Size (pgt.pos_size.Size)

    - Element                    (pgt.element.Element)
    - AniElement                 (pgt.element.AniElement)
    - MouseInteractionElement    (pgt.element.MouseInteractionElement)
    - MouseInteractionAniElement (pgt.element.MouseInteractionAniElement)

    - Lang (lang.Lang)

    - ani.FuncAniFrames (pgt.ani.FuncAniFrames)
    - ani.AniBase       (pgt.ani.AniBase)
    - ani.FuncAniBase   (pgt.ani.FuncAniBase)
    - ani.TextureAni    (pgt.ani.TextureAni)
    - ani.PosAni        (pgt.ani.PosAni)
    - ani.TextAni       (pgt.ani.TextAni)

    - gui.Label             (pgt.gui.label.Label)
    - gui.AniLabel          (pgt.gui.label.AniLabel)
    - gui.SurfaceElement    (pgt.gui.surface_element.SurfaceElement)
    - gui.AniSurfaceElement (pgt.gui.surface_element.AniSurfaceElement)

    - Pos  (pgt.pos_size.Pos)
    - Size (pgt.pos_size.Size)

    - Stack (pgt.stack.Stack)

Exceptions:
    - InvalidPosError (pgt.exceptions.InvalidPosError)
    - EmptyStackError (pgt.exceptions.EmptyStackError)

Functions:
    - add_col    (pgt.color.add_col)
    - sub_col    (pgt.color.sub_col)
    - mul_col    (pgt.color.mul_col)
    - min_col    (pgt.color.min_col)
    - max_col    (pgt.color.max_col)
    - calc_alpha (pgt.color.calc_alpha)
    - GRAY       (pgt.color.GRAY)
    - R          (pgt.color.R)
    - G          (pgt.color.G)
    - B          (pgt.color.B)

    - clamp            (pgt.mathf.clamp)
    - get_i            (pgt.mathf.clamp)
    - get_c            (pgt.mathf.clamp)
    - distance         (pgt.mathf.clamp)
    - abs_distance     (pgt.mathf.clamp)
    - e_in_sin         (pgt.mathf.e_in_sin)
    - e_out_sin        (pgt.mathf.e_out_sin)
    - e_in_out_sin     (pgt.mathf.e_in_out_sin)
    - e_in_quad        (pgt.mathf.e_in_quad)
    - e_out_quad       (pgt.mathf.e_out_quad)
    - e_in_out_quad    (pgt.mathf.e_in_out_quad)
    - e_in_cubic       (pgt.mathf.e_in_cubic)
    - e_out_cubic      (pgt.mathf.e_out_cubic)
    - e_in_out_cubic   (pgt.mathf.e_in_out_cubic)
    - e_in_quart       (pgt.mathf.e_in_quart)
    - e_out_quart      (pgt.mathf.e_out_quart)
    - e_in_out_quart   (pgt.mathf.e_in_out_quart)
    - e_in_quint       (pgt.mathf.e_in_quint)
    - e_out_quint      (pgt.mathf.e_out_quint)
    - e_in_out_quint   (pgt.mathf.e_in_out_quint)
    - e_in_exp         (pgt.mathf.e_in_exp)
    - e_out_exp        (pgt.mathf.e_out_exp)
    - e_in_out_exp     (pgt.mathf.e_in_out_exp)
    - e_in_circ        (pgt.mathf.e_in_circ)
    - e_out_circ       (pgt.mathf.e_out_circ)
    - e_in_out_circ    (pgt.mathf.e_in_out_circ)
    - e_in_back        (pgt.mathf.e_in_back)
    - e_out_back       (pgt.mathf.e_out_back)
    - e_in_out_back    (pgt.mathf.e_in_out_back)
    - e_in_elastic     (pgt.mathf.e_in_elastic)
    - e_out_elastic    (pgt.mathf.e_out_elastic)
    - e_in_out_elastic (pgt.mathf.e_in_out_elastic)
    - e_in_bounce      (pgt.mathf.e_in_bounce)
    - e_out_bounce     (pgt.mathf.e_out_bounce)
    - e_in_out_bounce  (pgt.mathf.e_in_out_bounce)

    - draw.clear_cache (pgt.draw.clear_cache)
    - draw.even_circle (pgt.draw.even_circle)
    - draw.odd_circle  (pgt.draw.odd_circle)
    - draw.aa_rect     (pgt.draw.aa_rect)

    - parse_json_file (pgt.utils.parse_json_file)
    - load_image      (pgt.utils.load_image)

Constants:
    - BLACK       (pgt.color.BLACK)
    - WHITE       (pgt.color.WHITE)
    - RED         (pgt.color.RED)
    - GREEN       (pgt.color.GREEN)
    - BLUE        (pgt.color.BLUE)
    - YELLOW      (pgt.color.YELLOW)
    - CYAN        (pgt.color.CYAN)
    - MAGENTA     (pgt.color.MAGENTA)
    - MAROON      (pgt.color.MAROON)
    - EMERALD     (pgt.color.EMERALD)
    - NAVY        (pgt.color.NAVY)
    - OLIVE       (pgt.color.OLIVE)
    - TEAL        (pgt.color.TEAL)
    - PURPURA     (pgt.color.PURPURA)
    - ORANGE      (pgt.color.ORANGE)
    - LIME        (pgt.color.LIME)
    - AQUA        (pgt.color.AQUA)
    - LIGHT_BLUE  (pgt.color.LIGHT_BLUE)
    - PURPLE      (pgt.color.PURPLE)
    - FUCHSIA     (pgt.color.FUCHSIA)
    - SALMON      (pgt.color.SALMON)
    - LIGHT_GREEN (pgt.color.LIGHT_GREEN)
    - COBALT      (pgt.color.COBALT)
    - LEMON       (pgt.color.LEMON)
    - SKY_BLUE    (pgt.color.SKY_BLUE)
    - PINK        (pgt.color.PINK)

    - Anc.UL (pgt.element.Anc.UL)
    - Anc.UC (pgt.element.Anc.UC)
    - Anc.UR (pgt.element.Anc.UR)
    - Anc.CL (pgt.element.Anc.CL)
    - Anc.CC (pgt.element.Anc.CC)
    - Anc.CR (pgt.element.Anc.CR)
    - Anc.DL (pgt.element.Anc.DL)
    - Anc.DC (pgt.element.Anc.DC)
    - Anc.DR (pgt.element.Anc.DR)

    - ani.PERC         (pgt.ani.PERC)
    - ani.PREV_VAL     (pgt.ani.PREV_VAL)
    - ani.STARTING_VAL (pgt.ani.STARTING_VAL)
    - ani.FRAME        (pgt.ani.FRAME)
    - ani.ANIMATION    (pgt.ani.ANIMATION)

    - draw.ODD_CIRCLE_CACHE  (pgt.draw.ODD_CIRCLE_CACHE)
    - draw.EVEN_CIRCLE_CACHE (pgt.draw.EVEN_CIRCLE_CACHE)
    - draw.RECT_CACHE        (pgt.draw.RECT_CACHE)

Variables:
    - draw.even_circle_cache (pgt.draw.even_circle_cache)
    - draw.even_circle_srufs (pgt.draw.even_circle_srufs)
    - draw.odd_circle_cache  (pgt.draw.odd_circle_cache)
    - draw.odd_circle_srufs  (pgt.draw.odd_circle_srufs)
    - draw.rect_cache        (pgt.draw.rect_cache)
    - draw.rect_srufs        (pgt.draw.rect_srufs)
"""

__author__ = "TheSilvered"
__version__ = "0.1.0"

from . import ani
from .color import *
from . import draw
from .element import Element, AniElement, Anc, MouseInteractionElement, MouseInteractionAniElement
from .exceptions import *
from .lang import Lang
from . import gui
from .mathf import *
from .pos_size import Pos, Size
from .stack import Stack
from .utils import *

print(f"Pygame tools by {__author__}, version: {__version__}")
