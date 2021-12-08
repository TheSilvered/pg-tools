import pygame
from .color import calc_alpha
from .mathf import get_i
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

def clear_cache(caches=RECT_CACHE | EVEN_CIRCLE_CACHE | ODD_CIRCLE_CACHE):
    if caches & ODD_CIRCLE_CACHE:
        odd_circle_cache.clear()
        odd_circle_srufs.clear()
    if caches & EVEN_CIRCLE_CACHE:
        even_circle_cache.clear()
        even_circle_srufs.clear()
    if caches & RECT_CACHE:
        rect_cache.clear()
        rect_srufs.clear()


def even_circle(surface, center, radius, color):
    blit_pos = (center[0] - radius, center[1] - radius)
    try:
        i = even_circle_cache.index([radius, color])
        surface.blit(even_circle_srufs[i], blit_pos)
        return
    except ValueError: pass

    new_surf = pygame.Surface((radius*2, radius*2), flags=pygame.SRCALPHA)
    new_surf.set_colorkey((0, 0, 0))
    using_alpha = len(color) == 4

    for x in range(radius):
        for y in range(radius):
            inv_x = radius*2 - x - 1
            inv_y = radius*2 - y - 1

            distance = get_i(x - radius, y - radius)

            if distance < radius:
                new_surf.set_at((x, y), color)
                new_surf.set_at((inv_x, y), color)
                new_surf.set_at((x, inv_y), color)
                new_surf.set_at((inv_x, inv_y), color)
            elif distance < radius + 1:
                if using_alpha:
                    alpha = color[3] * (1 - (distance-radius))
                else:
                    alpha = 255 * (1 - (distance-radius))
                new_color = tuple(color[:3]) + (alpha,)
                new_surf.set_at((x, y), new_color)
                new_surf.set_at((inv_x, y), new_color)
                new_surf.set_at((x, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

    surface.blit(new_surf, blit_pos)
    even_circle_cache.append([radius, color])
    even_circle_srufs.append(new_surf)


def odd_circle(surface, center, radius, color):
    blit_pos = (center[0] - radius, center[1] - radius)
    try:
        i = odd_circle_cache.index([radius, color])
        surface.blit(odd_circle_srufs[i], blit_pos)
        return
    except ValueError: pass

    size = ((radius+1)*2, (radius+1)*2)

    new_surf = pygame.Surface(size, flags=pygame.SRCALPHA)
    new_surf.set_colorkey((0, 0, 0))
    using_alpha = len(color) == 4

    for x in range(radius):
        for y in range(radius):
            inv_x = radius*2 - x
            inv_y = radius*2 - y

            distance = get_i(x - radius, y - radius)

            if distance < radius:
                new_surf.set_at((x, y), color)
                new_surf.set_at((inv_x, y), color)
                new_surf.set_at((x, inv_y), color)
                new_surf.set_at((inv_x, inv_y), color)
            elif distance < radius + 1:
                if using_alpha:
                    alpha = color[3] * (1 - (distance-radius))
                else:
                    alpha = 255 * (1 - (distance-radius))
                new_color = tuple(color[:3]) + (alpha,)
                new_surf.set_at((x, y), new_color)
                new_surf.set_at((inv_x, y), new_color)
                new_surf.set_at((x, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

    pygame.draw.line(new_surf, color, (radius, 0), (radius, radius*2))
    pygame.draw.line(new_surf, color, (0, radius), (radius*2, radius))

    surface.blit(new_surf, blit_pos)
    odd_circle_cache.append([radius, color])
    odd_circle_srufs.append(new_surf)


def aa_rect(surface, rect, color, corner_radius=0, line_c=None, width=0):
    try:
        i = rect_cache.index([rect.size, color, corner_radius, line_c, width])
        surface.blit(rect_srufs[i], rect.topleft)
        return
    except ValueError: pass

    new_surf = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
    new_surf.set_colorkey((0, 0, 0))
    using_alpha = len(color) == 4
    if line_c is not None and using_alpha: line_c = line_c[:3] + (color[3],)
    line_rect = pygame.Rect(0, 0, rect.w, rect.h)
    inner_rect = pygame.Rect(width, width, rect.w - width*2, rect.h - width*2)

    inner_radius = corner_radius - width

    if width:
        pygame.draw.rect(new_surf, line_c, line_rect, 0, corner_radius)
    pygame.draw.rect(new_surf, color, inner_rect, 0, inner_radius)

    for x in range(corner_radius):
        if not width: break
        for y in range(corner_radius):
            inv_x = rect.w - x - 1
            inv_y = rect.h - y - 1

            distance = get_i(x - corner_radius, y - corner_radius)

            if distance < corner_radius:
                new_surf.set_at((x, y), line_c)
                new_surf.set_at((inv_x, y), line_c)
                new_surf.set_at((x, inv_y), line_c)
                new_surf.set_at((inv_x, inv_y), line_c)
            elif distance < corner_radius + 1:
                if using_alpha:
                    alpha = color[3] * (1 - (distance-corner_radius))
                else:
                    alpha = 255 * (1 - (distance-corner_radius))
                new_color = tuple(line_c[:3]) + (alpha,)
                new_surf.set_at((x, y), new_color)
                new_surf.set_at((inv_x, y), new_color)
                new_surf.set_at((x, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

    for x in range(inner_radius):
        for y in range(inner_radius):
            inv_x = rect.w - x - 1 - width
            inv_y = rect.h - y - 1 - width

            distance = get_i(x - inner_radius, y - inner_radius)

            if distance < inner_radius:
                new_surf.set_at((x + width, y + width), color)
                new_surf.set_at((inv_x, y + width), color)
                new_surf.set_at((x + width, inv_y), color)
                new_surf.set_at((inv_x, inv_y), color)
            elif distance < inner_radius + 1:
                if width:
                    alpha = 1 - (distance-inner_radius)
                    new_color = calc_alpha(color, line_c, alpha)
                    if using_alpha: new_color += (color[3],)
                else:
                    if using_alpha:
                        alpha = color[3] * (1 - (distance-inner_radius))
                    else:
                        alpha = 255 * (1 - (distance-inner_radius))
                    new_color = tuple(color[:3]) + (alpha,)
                new_surf.set_at((x + width, y + width), new_color)
                new_surf.set_at((inv_x, y + width), new_color)
                new_surf.set_at((x + width, inv_y), new_color)
                new_surf.set_at((inv_x, inv_y), new_color)

    surface.blit(new_surf, rect.topleft)
    rect_cache.append([rect.size, color, corner_radius, line_c, width])
    rect_srufs.append(new_surf)
