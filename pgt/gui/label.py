import pygame
from pgt.element import Element, AniElement
from .font import Font


class Label(Element):
    def __init__(self,
       text="",
       text_size=20,
       color=None,
       bg_color=None,
       font=None,
       style="",
       alignment="left",
       line_height=None,
       adapt_to_width=False,
       exceed_size=True,
       auto_size=False,
       *args, **kwargs):

        super().__init__(*args, **kwargs)

        style = style.split(" ")
        self._aa = not "no_aa" in style
        if not self._aa: style.remove("no_aa")

        if isinstance(font, pygame.font.Font):
            self.font = font
            self.pygame_font = True
        elif isinstance(font, Font):
            self.font = font
            self.pygame_font = False
        else:
            try:
                self.font = pygame.font.Font(font, text_size)
            except FileNotFoundError:
                self.font = pygame.font.SysFont(font, text_size)
            self.pygame_font = True

        if "bold" in style and self.pygame_font:
            self.font.set_bold(True)
        if "italic" in style and self.pygame_font:
            self.font.set_italic(True)
        if "underline" in style and self.pygame_font:
            self.font.set_underline(True)

        self.__text = text
        self.adapt_width = adapt_to_width
        self.exceed_size = exceed_size
        self.alignment = alignment
        self.lines = None
        self.auto_size = auto_size

        if color is None: color = (1, 1, 1)
        self.color = color
        if bg_color is None: bg_color = (0, 0, 0)
        self.bg_color = bg_color

        if not self.alignment in ("left", "right", "center", "centre"):
            self.alignment = "left"

        if line_height is None:
            self._line_h = self.font.get_linesize()
        else:
            self._line_h = line_height

        self.text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = str(text)

        self.lines = self.__text.split("\n")
        if self.lines[-1] == "": del self.lines[-1]

        if self.adapt_width:
            new_lines = []
            for l in self.lines:
                words = l.split(" ")
                current_text = words[0]
                prev_text = words[0]
                for word in words[1:]:
                    current_text = current_text + " " + word
                    if self.font.size(current_text)[0] > self.size.w:
                        new_lines.append(prev_text)
                        current_text = word
                        prev_text = word
                        continue
                    prev_text = current_text
                if self.font.size(current_text)[0] > self.size.w:
                    new_lines.append(prev_text)
                else:
                    new_lines.append(current_text)
            self.lines = new_lines

        if not self.lines: self.lines = [""]

        if self.exceed_size:
            width = max([self.font.size(i)[0] for i in self.lines])
            height = self._line_h * len(self.lines)
            new_image = pygame.Surface((width, height), flags=pygame.SRCALPHA)
        else:
            new_image = pygame.Surface(self.size, flags=pygame.SRCALPHA)
        new_image.set_colorkey((0, 0, 0))

        for l_no, i in enumerate(self.lines):
            if self.pygame_font:
                line = self.font.render(i, self._aa, self.color)
            else:
                line = self.font.render(i, self.color, self.bg_color, self._aa)
            y = self._line_h * l_no
            if self.alignment == "left":
                new_image.blit(line, (0, y))
            elif self.alignment == "right":
                x = new_image.get_width() - self.font.size(i)[0]
                new_image.blit(line, (x, y))
            else:
                x = (new_image.get_width() - self.font.size(i)[0]) // 2
                new_image.blit(line, (x, y))

        self.change_image(new_image)

    def rotate(self, *args, **kwargs):
        if self.auto_size:
            super().rotate(*args, **kwargs)
        else:
            prev_size = self.size.copy()
            super().rotate(*args, **kwargs)
            self.size = prev_size


class AniLabel(Label, AniElement):
    pass
