# Amelia Hronowsky
# 101142991
# Team 65

from Cimpl import create_image, create_color, set_color, get_color
from T65_P4_posterize import posterize_filter
from test_invert import check_equal


def test_posterize_filter() -> None:
    '''A test function for posterize filter.

    Author: Amelia Hronowsky 101142991

    >>> test_posterize_filter()
    '''

    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(31, 31, 31))
    set_color(expected, 1, 0,  create_color(31, 31, 31))
    set_color(expected, 2, 0,  create_color(95, 95, 95))
    set_color(expected, 3, 0,  create_color(95, 95, 223))
    set_color(expected, 4, 0,  create_color(223, 223, 223))
    set_color(expected, 5, 0,  create_color(223, 223, 223))

    poster_color = posterize_filter(original)
    for x, y, col in poster_color:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


if __name__ == "__main__":
    test_posterize_filter()
