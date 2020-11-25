# Quinn Parrott
# 101169535
# Team 65

from T65_P5_edge import detect_edges
from test_invert import check_equal
from Cimpl import create_image, create_color, set_color, get_color

BLACK = create_color(0, 0, 0)
WHITE = create_color(255, 255, 255)


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


if __name__ == "__main__":
    test_edge_detect()
