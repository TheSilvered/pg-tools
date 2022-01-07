from typing import Optional, Union
from os import PathLike
import json

from pygame import Surface
from pygame.image import load

from .type_hints import _col_type, _size


def parse_json_file(path: Union[str, PathLike],
                    encoding: str = "utf-8") -> Union[list, dict]:
    """
    parse_json_file

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
    load_image

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
        if surface: return load(path).convert_alpha(surface)
        return load(path).convert_alpha()
    else:
        return load(path).convert()


def filled_surface(size: _size, color: _col_type, flags: int = 0) -> Surface:
    """
    filled_surface

    Type: function

    Description: returns a new surface filled with the specified color

    Args:
        'size' (Sequence): the size of the surface
        'color' (pygame.Color): the color of the surface
        'flags' (int): additional flags for the surface
    """
    surf = Surface(size, flags)
    surf.fill(color)
    return surf


def replace_color(surface: Surface, col1: _col_type, col2: _col_type) -> Surface:
    """
    replace_color

    Type: function

    Description: creates a new surface replacing one color from the old one

    Args:
        'surface' (pygame.Surface): the original surface
        'col1' (pygame.Color): the color to replace
        'col2' (pygame.Color): the color that replaces the old one
    """
    pixel_arr = pygame.PixelArray(surface.copy())
    pixel_arr.replace(col1, col2)
    new_img = pixel_arr.surface.copy()
    new_img.unlock()
    return new_img
