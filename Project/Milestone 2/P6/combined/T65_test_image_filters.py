# Team 65
# Members:
# -Amelia Hronowsky 101142991
# -Quinn Parrott 101169535
# -Ifeoluwa Shonibare 101145333
# -Tawseef Patel 101145333

from Cimpl import create_image, Color, create_color, set_color, get_color
from test_invert import check_equal
from T65_image_filters import red_channel, green_channel, blue_channel,\
    combine_filter, posterize_filter, sepia_filter, extreme_contrast,\
    two_toned, three_toned, detect_edges, detect_edges_better,\
    flip_horizontal, flip_vertical


BLACK = create_color(0, 0, 0)
WHITE = create_color(255, 255, 255)


def test_extreme() -> None:
    """
    A test function for extreme contrast filter

    Author: Tawseef Patel 101145333

    >>> test_extreme()
    """
    original = create_image(4, 1)
    set_color(original, 0, 0,  create_color(25, 126, 200))
    set_color(original, 1, 0,  create_color(200, 130, 10))

    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 255))
    set_color(expected, 1, 0,  create_color(255, 255, 0))

    contrast_image = extreme_contrast(original)
    for x, y, col in contrast_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_posterize_filter() -> None:
    """
    A test function for posterize filter.

    Author: Amelia Hronowsky 101142991

    >>> test_posterize_filter()
    """
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


def test_three_tone() -> None:
    """
    Returns 'PASSED' if pixels from three_tone match with the calculated pixels
    from expected_image

    Author: Ifeoluwa Shonibare 101164650

    >>> test_three_tone()
    """
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(47, 3, 66))
    set_color(original, 1, 0,  create_color(120, 33, 175))
    set_color(original, 2, 0,  create_color(201, 227, 186))

    expected_1 = create_image(3, 1)
    set_color(expected_1, 0, 0,  create_color(0, 0, 0))
    set_color(expected_1, 1, 0,  create_color(255, 255, 255))
    set_color(expected_1, 2, 0,  create_color(255, 0, 0))

    three_tone_image = three_toned(original, "black", "white", "red")
    for x, y, col in three_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_1, x, y))

    expected_2 = create_image(3, 1)
    set_color(expected_2, 0, 0,  create_color(0, 255, 0))
    set_color(expected_2, 1, 0,  create_color(0, 0, 255))
    set_color(expected_2, 2, 0,  create_color(255, 255, 0))

    three_tone_image = three_toned(original, "lime", "blue", "yellow")
    for x, y, col in three_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_2, x, y))

    expected_3 = create_image(3, 1)
    set_color(expected_3, 0, 0,  create_color(0, 255, 255))
    set_color(expected_3, 1, 0,  create_color(255, 0, 255))
    set_color(expected_3, 2, 0,  create_color(128, 128, 128))

    three_tone_image = three_toned(original, "cyan", "magenta", "gray")
    for x, y, col in three_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_3, x, y))


def test_two_tone() -> None:
    """
    Returns 'PASSED' if pixels from two_tone match with the calculated pixels
    from expected_image

    Author: Ifeoluwa Shonibare 101164650

    >>> test_two_tone()
    """
    original = create_image(2, 1)
    set_color(original, 0, 0,  create_color(47, 89, 198))
    set_color(original, 1, 0,  create_color(111, 77, 215))

    expected_1 = create_image(2, 1)
    set_color(expected_1, 0, 0,  create_color(255, 255, 255))
    set_color(expected_1, 1, 0,  create_color(0, 0, 0))

    two_tone_image = two_toned(original, "white", "black")
    for x, y, col in two_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_1, x, y))

    expected_2 = create_image(2, 1)
    set_color(expected_2, 0, 0,  create_color(255, 0, 0))
    set_color(expected_2, 1, 0,  create_color(0, 255, 0))

    two_tone_image = two_toned(original, "red", "lime")
    for x, y, col in two_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_2, x, y))

    expected_3 = create_image(2, 1)
    set_color(expected_3, 0, 0,  create_color(0, 0, 255))
    set_color(expected_3, 1, 0,  create_color(255, 255, 0))

    two_tone_image = two_toned(original, "blue", "yellow")
    for x, y, col in two_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_3, x, y))

    expected_4 = create_image(2, 1)
    set_color(expected_4, 0, 0,  create_color(0, 255, 255))
    set_color(expected_4, 1, 0,  create_color(255, 0, 255))

    two_tone_image = two_toned(original, "cyan", "magenta")
    for x, y, col in two_tone_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_4, x, y))


def test_edge_detect() -> None:
    """
    Test the edge detection filter

    Author: Quinn Parrott 101169535

    >>> test_edge_detect()
    """
    original = create_image(1, 5)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(2, 1, 0))
    set_color(original, 0, 2, create_color(8, 8, 8))
    set_color(original, 0, 3, create_color(100, 100, 100))
    set_color(original, 0, 4, create_color(112, 112, 112))

    # At threshold 5
    expected_thr1 = create_image(1, 5)
    set_color(expected_thr1, 0, 0, WHITE)
    set_color(expected_thr1, 0, 1, BLACK)
    set_color(expected_thr1, 0, 2, BLACK)
    set_color(expected_thr1, 0, 3, BLACK)
    set_color(expected_thr1, 0, 4, WHITE)

    # At threshold 10
    expected_thr2 = create_image(1, 5)
    set_color(expected_thr2, 0, 0, WHITE)
    set_color(expected_thr2, 0, 1, WHITE)
    set_color(expected_thr2, 0, 2, BLACK)
    set_color(expected_thr2, 0, 3, BLACK)
    set_color(expected_thr2, 0, 4, WHITE)

    # At threshold 15
    expected_thr3 = create_image(1, 5)
    set_color(expected_thr3, 0, 0, WHITE)
    set_color(expected_thr3, 0, 1, WHITE)
    set_color(expected_thr3, 0, 2, BLACK)
    set_color(expected_thr3, 0, 3, WHITE)
    set_color(expected_thr3, 0, 4, WHITE)

    threshold_test = [
        (expected_thr1, 5),
        (expected_thr2, 10),
        (expected_thr3, 15),
    ]

    for expected_image, threshold in threshold_test:
        post_process = detect_edges(original, threshold)
        for x, y, color in post_process:
            check_equal(
                f'Checking pixel @({x}, {y}) from threshold {threshold}',
                color, get_color(expected_image, x, y)
            )


def flip_horizontal_test() -> None:
    """
    A test function for flip_horizontal filter.

    Author: Tawseef Patel 101145333

    >>> flip_horizontal_test()
    """
    original_image = create_image(2, 4)

    set_color(original_image, 0, 0, create_color(0, 0, 0))
    set_color(original_image, 0, 1, create_color(255, 255, 255))
    set_color(original_image, 0, 2, create_color(0, 0, 0))
    set_color(original_image, 0, 3, create_color(255, 255, 255))
    set_color(original_image, 1, 0, create_color(255, 255, 255))
    set_color(original_image, 1, 1, create_color(0, 0, 0))
    set_color(original_image, 1, 2, create_color(255, 255, 255))
    set_color(original_image, 1, 3, create_color(0, 0, 0))

    expected_image = create_image(2, 4)

    set_color(expected_image, 0, 0, create_color(255, 255, 255))
    set_color(expected_image, 0, 1, create_color(0, 0, 0))
    set_color(expected_image, 0, 2, create_color(255, 255, 255))
    set_color(expected_image, 0, 3, create_color(0, 0, 0))
    set_color(expected_image, 1, 0, create_color(0, 0, 0))
    set_color(expected_image, 1, 1, create_color(255, 255, 255))
    set_color(expected_image, 1, 2, create_color(0, 0, 0))
    set_color(expected_image, 1, 3, create_color(255, 255, 255))

    horizontal_image = flip_horizontal(original_image)
    for x, y, col in horizontal_image:
        check_equal("Checking pixel @(" + str(x) + ', ' + str(y) + ')', col,
                    get_color(expected_image, x, y))


def test_flip_vertical() -> None:
    """
    A test function for vertical flip filter.

    Author: Amelia Hronowsky 101142991

    >>> test_flip_vertical()
    """
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 0,  create_color(254, 255, 255))
    set_color(expected, 2, 0,  create_color(125, 73, 224))
    set_color(expected, 3, 0,  create_color(127, 127, 127))
    set_color(expected, 4, 0,  create_color(0, 0, 1))
    set_color(expected, 5, 0,  create_color(0, 0, 0))

    vertical_image = flip_vertical(original)
    for x, y, col in vertical_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_imp_edge() -> None:
    """
    Returns 'PASSED' if pixels from detect_edges_better match with
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


def test_red_channel() -> None:
    """
    Checks if the G and B pixels are equal to 0 and only red is present

    Author: Tawseef Patel 101145333

    >>> test_red_channel()
    """
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(1, 0, 0))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(1, 0, 0))
    set_color(expected, 2, 0, create_color(127, 0, 0))
    set_color(expected, 3, 0, create_color(125, 0, 0))
    set_color(expected, 4, 0, create_color(254, 0, 0))
    set_color(expected, 5, 0, create_color(255, 0, 0))

    red = red_channel(original)
    for x, y, col in red:
        check_equal('Checking pixel @(' + str(x) + ',' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_green_channel() -> None:
    """
    Returns 'PASSED' if pixels from green_channel
    change the original pixels to the expected pixels

    Author: Ifeoluwa Shonibare 101145333

    >>> test_green_channel()
    """
    original = create_image(4, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 140, 224))

    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(0, 127, 0))
    set_color(expected, 3, 0,  create_color(0, 140, 0))

    green_image = green_channel(original)
    for x, y, col in green_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_blue_channel() -> None:
    """
    A test function for blue filter. Returns PASSED if no pixel components
    are red and green and failed otherwise.

    Author: Amelia Hronowsky 101142991

    >>> test_blue_channel()
    """
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 1))
    set_color(expected, 2, 0,  create_color(0, 0, 127))
    set_color(expected, 3, 0,  create_color(0, 0, 224))
    set_color(expected, 4, 0,  create_color(0, 0, 255))
    set_color(expected, 5, 0,  create_color(0, 0, 255))

    blue = blue_channel(original)
    for x, y, col in blue:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_combine_filter() -> None:
    """
    Test the combine filter

    Author: Quinn Parrott 101169535

    >>> test_combine_filter()
    """
    red_channel = create_image(2, 2)
    set_color(red_channel, 0, 0, Color(0, 10, 4))
    set_color(red_channel, 1, 0, Color(2, 4, 0))
    set_color(red_channel, 0, 1, Color(20, 0, 0))
    set_color(red_channel, 1, 1, Color(0, 0, 0))

    green_channel = create_image(2, 2)
    set_color(green_channel, 0, 0, Color(10, 0, 10))
    set_color(green_channel, 1, 0, Color(1, 5, 6))
    set_color(green_channel, 0, 1, Color(0, 20, 0))
    set_color(green_channel, 1, 1, Color(0, 0, 0))

    blue_channel = create_image(2, 2)
    set_color(blue_channel, 0, 0, Color(100, 100, 0))
    set_color(blue_channel, 1, 0, Color(9, 8, 7))
    set_color(blue_channel, 0, 1, Color(0, 0, 20))
    set_color(blue_channel, 1, 1, Color(0, 0, 0))

    result = combine_filter(red_channel, green_channel, blue_channel)

    expected_image = create_image(2, 2)
    set_color(expected_image, 0, 0, Color(0, 0, 0))
    set_color(expected_image, 1, 0, Color(2, 5, 7))
    set_color(expected_image, 0, 1, Color(20, 20, 20))
    set_color(expected_image, 1, 1, Color(0, 0, 0))

    for x, y, color in result:
        expected_color = get_color(expected_image, x, y)

        check_equal(f"Checking pixel @({x}, {y})", color, expected_color)


if __name__ == '__main__':
    # Testing
    print("Running tests...")
    print("Testing red channel")
    test_red_channel()
    print("Testing green channel")
    test_green_channel()
    print("Testing blue channel")
    test_blue_channel()
    print("Testing combine channel")
    test_combine_filter()
    print("Testing extreme contrast")
    test_extreme()
    print("Testing posterize")
    test_posterize_filter()
    print("Testing sepia")
    test_sepia_filter()
    print("Testing three tone")
    test_three_tone()
    print("Testing two tone")
    test_two_tone()
    print("Testing edge detect")
    test_edge_detect()
    print("Testing horizontal")
    flip_horizontal_test()
    print("Testing vertical")
    test_flip_vertical()
    print("Testing improved edge detect")
    test_imp_edge()
    print("Testing done successfully.")
