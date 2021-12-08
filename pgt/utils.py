from pygame.image import load
import json

def parse_json_file(path, encoding="utf-8"):
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

def load_image(path, has_alpha=False, surface=None):
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
