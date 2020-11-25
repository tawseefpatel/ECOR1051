
from Cimpl import create_image, create_color, set_color, get_color
from test_grayscale import check_equal
from T65_P5_imp_edge import detect_edges_better


def test_imp_edge() -> None:
    """Returns 'PASSED' if pixels from detect_edges_better match with
    the calculated pixels from expected_image

    Author: Ifeoluwa Shonibare 101164650

    >>> test_imp_edge()
    """
    original = create_image(4, 4)
    set_color(original, 0, 0, create_color(47, 3, 66))
    set_color(original, 1, 0, create_color(120, 33, 175))
    set_color(original, 2, 0, create_color(33, 55, 236))
    set_color(original, 3, 0, create_color(201, 90, 186))
    set_color(original, 0, 1, create_color(88, 1, 47))
    set_color(original, 1, 1, create_color(115, 234, 18))
    set_color(original, 2, 1, create_color(20, 2, 6))
    set_color(original, 3, 1, create_color(101, 145, 93))
    set_color(original, 0, 2, create_color(55, 227, 16))
    set_color(original, 1, 2, create_color(21, 27, 86))
    set_color(original, 2, 2, create_color(49, 64, 81))
    set_color(original, 3, 2, create_color(100, 121, 144))
    set_color(original, 0, 3, create_color(169, 225, 4))
    set_color(original, 1, 3, create_color(9, 16, 25))
    set_color(original, 2, 3, create_color(222, 167, 130))
    set_color(original, 3, 3, create_color(99, 38, 60))

    expected = create_image(4, 4)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 0, 1, create_color(0, 0, 0))
    set_color(expected, 1, 1, create_color(0, 0, 0))
    set_color(expected, 2, 1, create_color(0, 0, 0))
    set_color(expected, 3, 1, create_color(0, 0, 0))
    set_color(expected, 0, 2, create_color(0, 0, 0))
    set_color(expected, 1, 2, create_color(0, 0, 0))
    set_color(expected, 2, 2, create_color(0, 0, 0))
    set_color(expected, 3, 2, create_color(0, 0, 0))
    set_color(expected, 0, 3, create_color(0, 0, 0))
    set_color(expected, 1, 3, create_color(0, 0, 0))
    set_color(expected, 2, 3, create_color(0, 0, 0))
    set_color(expected, 3, 3, create_color(255, 255, 255))

    three_tone_image = detect_edges_better(original, 3)
    for x, y, col in three_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


if __name__ == "__main__":
    test_imp_edge()
