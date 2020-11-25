# Quinn Parrott
# 101169535
# Team 65
from T65_P4_sepia import sepia_filter
from test_invert import check_equal
from Cimpl import create_image, create_color, set_color, get_color


def test_sepia_filter() -> None:
    """
    Test the sepia filter

    Author: Quinn Parrott 101169535

    >>> test_sepia_filter()
    """
    original = create_image(4, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(40, 60, 20))
    set_color(original, 2, 0, create_color(127, 27, 227))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 0, 1, create_color(62, 62, 62))
    set_color(original, 1, 1, create_color(63, 63, 63))
    set_color(original, 2, 1, create_color(191, 191, 191))
    set_color(original, 3, 1, create_color(192, 192, 192))

    # Rounded to nearest integer
    expected = create_image(4, 2)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(44, 40, 36))
    set_color(expected, 2, 0, create_color(146, 127, 108))
    set_color(expected, 3, 0, create_color(161, 140, 119))
    set_color(expected, 0, 1, create_color(68, 62, 56))
    set_color(expected, 1, 1, create_color(72, 63, 54))
    set_color(expected, 2, 1, create_color(220, 191, 162))
    set_color(expected, 3, 1, create_color(207, 192, 179))

    sepia = sepia_filter(original)
    for x, y, color in sepia:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    color, get_color(expected, x, y))


if __name__ == "__main__":
    test_sepia_filter()
