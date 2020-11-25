# Quinn Parrott
# 101169535
# Team 65
from Cimpl import create_image, Image, get_width, get_height,\
    set_color, create_color

def _adjust_component(component: int, color_space_size: int = 4) -> int:
    """
    Return the downsized color space of a 256 value component. The
    number of possible values is given by 'color_space_size' (default: 4).

    Precondition:
    'component' must be between 0-255 inclusive
    'color_space_size' must be >1

    Author: Quinn Parrott 101169535

    >>> _adjust_component(0)
    31
    >>> _adjust_component(63)
    31
    >>> _adjust_component(64)
    95
    >>> _adjust_component(127)
    95
    >>> _adjust_component(128)
    159
    >>> _adjust_component(191)
    159
    >>> _adjust_component(192)
    223
    >>> _adjust_component(255)
    223
    """
    sector_size = 256 // color_space_size
    # First part is getting the sector number, the second part is the offset to
    # the sector midpoint
    return sector_size*(component//sector_size) + (sector_size//2 - 1)


def posterize_filter(image: Image) -> Image:
    """
    Return a Image with it's color space reduced to 4 possible values per
    component.

    Author: Quinn Parrott 101169535

    >>> from Cimpl import *
    >>> image = load_image(choose_file())
    >>> posterized = posterize_filter(image)
    >>> show(posterized)
    """
    # Allocated the  image
    poster_image = create_image(get_width(image), get_height(image))

    for x, y, (r, g, b) in image:
        poster_color = create_color(
            _adjust_component(r),
            _adjust_component(g),
            _adjust_component(b),
        )

        set_color(poster_image, x, y, poster_color)

    return poster_image


if __name__ == "__main__":
    from Cimpl import load_image, choose_file, show
    image = load_image(choose_file())
    posterized = posterize_filter(image)
    show(posterized)
