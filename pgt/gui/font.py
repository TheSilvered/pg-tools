import pygame
from pgt.pos_size import Size
from pgt.color import GRAY
pygame.init()

class Font:
    def __init__(self, image, chars_order, chars_widths, size=None):
        if len(chars_order) != len(chars_widths):
            raise ValueError("chars_order and chars_widths must have "
                             "the same length") from None

        self.chars = {}

        if size is not None and size != 0:
            size_mul = size / image.get_height()
            new_size = Size(image.get_size()) * size_mul
            image = pygame.transform.scale(image, new_size.int())
        else:
            size_mul = 1

        y = 0
        h = image.get_height()

        for ch, w_idx in zip(chars_order, range(len(chars_widths))):
            x = int(sum(chars_widths[:w_idx]) * size_mul)
            w = int(chars_widths[w_idx] * size_mul)
            rect = pygame.Rect(x, y, w, h)
            self.chars[ch] = (image.subsurface(rect), w)

        nochar_x = int(sum(chars_widths) * size_mul)
        nochar_w = image.get_width() - nochar_x
        self.nochar = (image.subsurface(nochar_x, y, nochar_w, h), nochar_w)
        self.line_size = h

    def get_linesize(self): return self.line_size

    def size(self, text):
        tot_width = sum(self.chars.get(i, self.nochar)[1] for i in str(text))

        return tot_width, self.line_size

    def render(self, text, text_c=(1, 1, 1), bg_c=(0, 0, 0), aa_colors=False):
        image = pygame.Surface(self.size(text), flags=pygame.SRCALPHA)
        image.set_colorkey((0, 0, 0))
        text = str(text)
        current_x = 0

        BG_COLOR = (0, 0, 0)
        COLOR = (255, 255, 255)

        text_c = pygame.Color(text_c)
        bg_c = pygame.Color(bg_c)

        for ch in text:
            surf = self.chars.get(ch, self.nochar)[0].convert_alpha(image)
            char_pixel_arr = pygame.PixelArray(surf.copy())
            if aa_colors:
                for i in range(255, -1, -1):
                    if bg_c == (0, 0, 0):
                        text_c.a = i
                        char_pixel_arr.replace(GRAY(i), text_c)
                        continue
                    char_pixel_arr.replace(GRAY(i), bg_c.lerp(text_c, i / 255))
            else:
                char_pixel_arr.replace(BG_COLOR, bg_c)
                char_pixel_arr.replace(COLOR, text_c)
            char_img = char_pixel_arr.surface.copy()
            char_img.unlock()
            image.blit(char_img, (current_x, 0))
            current_x += self.chars.get(ch, self.nochar)[1]

        return image
