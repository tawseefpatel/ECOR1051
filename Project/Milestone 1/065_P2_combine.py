"""
combine filter

@author Quinn Parrott
"""

from Cimpl import load_image, show, create_image, set_color, get_color, get_width, get_height, Image, Color


def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.

    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.

    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal.
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


def combine_filter(red_channel: Image, green_channel: Image, blue_channel: Image) -> Image:
    """
    Return an Image that is a combination of red, green and blue channel of three other images.

    Precondition:
    All images must be the same size.

    >>> red_image = load_image(choose_file())
    >>> green_image = load_image(choose_file())
    >>> blue_image = load_image(choose_file())
    >>> combined = combine_filter(red_image, green_image, blue_image)
    >>> show(combined)
    """
    # Allocated the combined image
    combined_image = create_image(get_width(red_channel), get_height(red_channel))

    for x, y, _ in combined_image:
        # Get the color from each channel
        red_color = get_color(red_channel, x, y)
        green_color = get_color(green_channel, x, y)
        blue_color = get_color(blue_channel, x, y)

        # Combining the colors together
        combined_color = Color(red_color[0], green_color[1], blue_color[2])

        set_color(combined_image, x, y, combined_color)

    return combined_image


def test_combine_filter():
    """
    Test the combine filter

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

# This checks with this was imported or is being run directly
# The test will only be performed when this file is run independently
if __name__ == '__main__':
    test_combine_filter()

    # The names of the image files
    filenames = [
            "red_image.png",
            "green_image.png",
            "blue_image.png"
    ]

    # Take each image filename and load the images into a list
    images = [load_image(filename) for filename in filenames]

    # Unpack the list of images into combine_filter then show the result
    show(combine_filter(*images))
