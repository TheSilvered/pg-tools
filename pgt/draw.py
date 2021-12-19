import pygame
from .color import calc_alpha
from .mathf import get_i
from .type_hints import _pos, _col_type
from typing import Optional
pygame.init()

even_circle_cache = []
even_circle_srufs = []
odd_circle_cache = []
odd_circle_srufs = []
rect_cache = []
rect_srufs = []

ODD_CIRCLE_CACHE = 0b001
EVEN_CIRCLE_CACHE = 0b010
RECT_CACHE = 0b100


def clear_cache(caches: int = RECT_CACHE | EVEN_CIRCLE_CACHE | ODD_CIRCLE_CACHE):
    if caches & ODD_CIRCLE_CACHE:
        odd_circle_cache.clear()
        odd_circle_srufs.clear()
    if caches & EVEN_CIRCLE_CACHE:
        even_circle_cache.clear()
        even_circle_srufs.clear()
    if caches & RECT_CACHE:
        rect_cache.clear()
        rect_srufs.clear()


def even_circle(surface: pygame.Surface,
                center: _pos,
                radius: int,
                color: _col_type,
                border: int = 0,
                border_color: Optional[_col_type] = None):

    blit_pos = (center[0] - radius, center[1] - radius)

    if radius - border < 0: border = radius

    try:
        i = even_circle_cache.index([radius, color])
        surface.blit(even_circle_srufs[i], blit_pos)
        return
    except ValueError: pass

    new_surf = pygame.Surface((radius*2, radius*2), flags=pygame.SRCALPHA)
    new_surf.set_colorkey((0, 0, 0))
    alpha_col = len(color) == 4
    alpha_b_col = border_color and len(border_color) == 4
    inner_radius = radius - border

    for x in range(radius):
        for y in range(radius):
            inv_x = radius*2 - x - 1
            inv_y = radius*2 - y - 1

            distance = get_i(x - radius, y - radius)

            if distance < inner_radius:
                new_surf.set_at((x, y), color)
                new_surf.set_at((inv_x, y), color)
                new_surf.set_at((x, inv_y), color)
                new_surf.set_at((inv_x, inv_y), color)

            elif border and distance < inner_radius + 1:
                alpha = 1 - (distance-inner_radius)
                new_color = calc_alpha(color, border_color, alpha)
                new_surf.set_at((x, y), new_color)
                new_surf.set_at((inv_x, y), new_color)
                new_surf.set_at((x, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

            elif distance < radius:
                new_surf.set_at((x, y), border_color)
                new_surf.set_at((inv_x, y), border_color)
                new_surf.set_at((x, inv_y), border_color)
                new_surf.set_at((inv_x, inv_y), border_color)

            elif distance < radius + 1:
                if border:
                    alpha = (border_color[3] if alpha_b_col else 255) * (1 - (distance - radius))
                    new_color = list(border_color[:3])
                else:
                    alpha = (color[3] if alpha_col else 255) * (1 - (distance - radius))
                    new_color = list(color[:3])
                new_color.append(alpha)

                new_surf.set_at((x, y), new_color)
                new_surf.set_at((inv_x, y), new_color)
                new_surf.set_at((x, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

    surface.blit(new_surf, blit_pos)
    even_circle_cache.append([radius, color])
    even_circle_srufs.append(new_surf)


def odd_circle(surface: pygame.Surface,
               center: _pos,
               radius: int,
               color: _col_type,
               border: int = 0,
               border_color: Optional[_col_type] = None):

    blit_pos = (center[0] - radius, center[1] - radius)
    try:
        i = odd_circle_cache.index([radius, color, border, border_color])
        surface.blit(odd_circle_srufs[i], blit_pos)
        return
    except ValueError: pass

    size = ((radius+1)*2, (radius+1)*2)

    new_surf = pygame.Surface(size, flags=pygame.SRCALPHA)
    new_surf.set_colorkey((0, 0, 0))
    alpha_col = len(color) == 4
    alpha_b_col = border_color and len(border_color) == 4
    inner_radius = radius - border

    for x in range(radius):
        for y in range(radius):
            inv_x = radius*2 - x
            inv_y = radius*2 - y

            distance = get_i(x - radius, y - radius)

            if distance < inner_radius:
                new_surf.set_at((x, y), color)
                new_surf.set_at((inv_x, y), color)
                new_surf.set_at((x, inv_y), color)
                new_surf.set_at((inv_x, inv_y), color)

            elif border and distance < inner_radius + 1:
                alpha = 1 - (distance-inner_radius)
                new_color = calc_alpha(color, border_color, alpha)
                new_surf.set_at((x, y), new_color)
                new_surf.set_at((inv_x, y), new_color)
                new_surf.set_at((x, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

            elif distance < radius:
                new_surf.set_at((x, y), border_color)
                new_surf.set_at((inv_x, y), border_color)
                new_surf.set_at((x, inv_y), border_color)
                new_surf.set_at((inv_x, inv_y), border_color)

            elif distance < radius + 1:
                if border:
                    alpha = (border_color[3] if alpha_b_col else 255) * (1 - (distance - radius))
                    new_color = list(border_color[:3])
                else:
                    alpha = (color[3] if alpha_col else 255) * (1 - (distance - radius))
                    new_color = list(color[:3])
                new_color.append(alpha)

                new_surf.set_at((x, y), new_color)
                new_surf.set_at((inv_x, y), new_color)
                new_surf.set_at((x, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

    pygame.draw.line(new_surf, border_color, (radius, 0), (radius, radius*2))
    pygame.draw.line(new_surf, border_color, (0, radius), (radius*2, radius))
    pygame.draw.line(new_surf, color, (radius, border), (radius, radius*2 - border))
    pygame.draw.line(new_surf, color, (border, radius), (radius*2 - border, radius))

    surface.blit(new_surf, blit_pos)
    odd_circle_cache.append([radius, color, border, border_color])
    odd_circle_srufs.append(new_surf)


def aa_rect(surface: pygame.Surface,
            rect: pygame.Rect,
            color: _col_type,
            corner_radius: int = 0,
            border: int = 0,
            border_color: Optional[_col_type] = None):
    if corner_radius > min(rect.width, rect.height) / 2:
        corner_radius = int(min(rect.width, rect.height) / 2)

    if border > min(rect.width, rect.height) / 2:
        border = int(min(rect.width, rect.height) / 2)

    try:
        i = rect_cache.index([rect.size, color, corner_radius, border, border_color])
        surface.blit(rect_srufs[i], rect.topleft)
        return
    except ValueError: pass

    new_surf = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    new_surf.set_colorkey((0, 0, 0))
    alpha_col = len(color) == 4
    alpha_b_col = border_color and len(border_color) == 4
    line_rect = pygame.Rect(0, 0, rect.w, rect.h)
    inner_rect = pygame.Rect(border, border, rect.w - border*2, rect.h - border*2)

    inner_radius = corner_radius - border

    if border:
        pygame.draw.rect(new_surf, border_color, line_rect, 0, corner_radius)
    pygame.draw.rect(new_surf, color, inner_rect, 0, inner_radius)

    for x in range(corner_radius):
        for y in range(corner_radius):
            inv_x = rect.w - x - 1
            inv_y = rect.h - y - 1

            distance = get_i(x - corner_radius, y - corner_radius)

            if distance < inner_radius:
                new_surf.set_at((x, y), color)
                new_surf.set_at((inv_x, y), color)
                new_surf.set_at((x, inv_y), color)
                new_surf.set_at((inv_x, inv_y), color)

            elif border and distance < inner_radius + 1:
                alpha = 1 - (distance-inner_radius)
                new_color = calc_alpha(color, border_color, alpha)
                new_surf.set_at((x, y), new_color)
                new_surf.set_at((inv_x, y), new_color)
                new_surf.set_at((x, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

            elif distance < corner_radius:
                new_surf.set_at((x, y), border_color)
                new_surf.set_at((inv_x, y), border_color)
                new_surf.set_at((x, inv_y), border_color)
                new_surf.set_at((inv_x, inv_y), border_color)

            elif distance < corner_radius + 1:
                if border:
                    alpha = (border_color[3] if alpha_b_col else 255) * (1 - (distance - corner_radius))
                    new_color = list(border_color[:3])
                else:
                    alpha = (color[3] if alpha_col else 255) * (1 - (distance - corner_radius))
                    new_color = list(color[:3])
                new_color.append(alpha)

                new_surf.set_at((x, y), new_color)
                new_surf.set_at((inv_x, y), new_color)
                new_surf.set_at((x, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

    surface.blit(new_surf, rect.topleft)
    rect_cache.append([rect.size, color, corner_radius, border, border_color])
    rect_srufs.append(new_surf)
