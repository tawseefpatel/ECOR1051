#Created by Tawseef Patel 101145333
#Team Number 65

from Cimpl import *
from T65_P5_flip_horizontal import *


def check_equal(description: str, outcome, expected) -> None:
    """
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")


def flip_horizontal_test() -> None:
    """A test function for flip_horizontal filter.
    >>> flip_horizontal_test()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    Checking pixel @(1, 2) PASSED
    ------
    Checking pixel @(0, 3) PASSED
    ------
    Checking pixel @(1, 3) PASSED
    ------
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

flip_horizontal_test()

