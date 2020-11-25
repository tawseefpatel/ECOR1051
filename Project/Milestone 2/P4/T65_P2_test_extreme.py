#Created by Tawseef Patel
#student number:101145333
#Team number 65

from Cimpl import *

from T65_P2_extreme import extreme_contrast

def check_equal(description: str, outcome, expected) -> None:
    """
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format method is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.

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

def test_extreme() -> None:
    '''A test function for extreme contrast filter

    >>> test_extreme()
    '''

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

test_extreme()