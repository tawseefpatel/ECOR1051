# Team 65
# Members:
# -Amelia Hronowsky 101142991
# -Quinn Parrott 101169535
# -Ifeoluwa Shonibare 101145333
# -Tawseef Patel 101145333

from Cimpl import *

"""
Changelog:
-Functions where renamed to have a consistent naming scheme
-2 very small typos where fixed
-Consistent docstring style with author's name
-Removed all superfluous imports
-Added team comment at the top
-Everything outside a function (that was not needed) was moved to the bottom
"""

def red_channel(file: Image)-> Image:
    """
    Returns the selected file with no G or B values. (Returns the file with only red pixels) 

    Author: Tawseef Patel 101145333
    """
    original_image = copy(file)
    for x, y, (r, g, b) in original_image:
        red_color = create_color(r, g-g, b-b)
        red_image = original_image
        colors = set_color(red_image, x,y, red_color) 

    return red_image

def test_red_channel()-> None:
    """
    Checks if the G and B pixels are equal to 0 and only red is present

    Author: Tawseef Patel 101145333

    >>>test_red(red_channel(image1))
    >>>Filter has Passed
    """
    original = create_image(6,1)
    set_color(original, 0, 0, create_color(0,0,0))
    set_color(original, 1, 0, create_color(1,0,0))
    set_color(original, 2, 0, create_color(127,127,127))
    set_color(original, 3, 0, create_color(125,73,224))
    set_color(original, 4, 0, create_color(254,255,255))
    set_color(original, 5, 0, create_color(255,255,255))
    
    expected = create_image(6,1)
    set_color(expected, 0, 0, create_color(0,0,0))
    set_color(expected, 1, 0, create_color(1,0,0))
    set_color(expected, 2, 0, create_color(127,0,0))
    set_color(expected, 3, 0, create_color(125,0,0))
    set_color(expected, 4, 0, create_color(254,0,0))
    set_color(expected, 5, 0, create_color(255,0,0))
    
    red = red_channel(original)
    for x, y, col in red:
        check_equal('Checking pixel @(' + str(x) + ','+ str(y) + ')', col, get_color(expected, x,y))


def green_channel(image: object) -> object:
    """
    Returns image with a green filter applied by changing every red and
    blue RGB value to 0 in each pixel

    Author: Ifeoluwa Shonibare 101145333
    """
    GREEN_PIC = copy(image)
    for pixel in GREEN_PIC:
        x, y, (r, g, b) = pixel
        green_color = create_color(0, g, 0)
        set_color(GREEN_PIC, x, y, green_color)
    return GREEN_PIC


def test_green_channel() -> None:
    """
    Returns 'PASSED' if pixels from green_channel
    change the original pixels to the expected pixels

    Author: Ifeoluwa Shonibare 101145333
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


def blue_channel(image: Image) -> Image:
    """
    Returns a copy of the original image with a blue filter, with zero green and red pixel components.

    Author: Amelia Hronowsky 101142991

    >>>image = load_image(choose_file())
    >>>blue_image = blue_channel(image)
    >>>show(blue_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        r, g, b = 0, 0, b
        blue = create_color(r, g, b)
        set_color(new_image, x, y, blue)
    return new_image


def test_blue_channel() -> None:
    '''
    A test function for blue filter. Returns PASSED if no pixel components
    are red and green and failed otherwise.

    Author: Amelia Hronowsky 101142991

    >>> test_blue_channel()
    '''

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


def combine_filter(red_channel: Image, green_channel: Image, blue_channel: Image) -> Image:
    """
    Return an Image that is a combination of red, green and blue channel of three other images.

    Precondition:
    All images must be the same size.

    Author: Quinn Parrott 101169535

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


# The test will only be performed when this file is run independently not when imported
if __name__ == '__main__':

    #image1 = choose_file()
    image_filename = "miss_sullivan.jpg"

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
    print("Testing done successfully.")

    # Loading images
    image = load_image(image_filename)

    # The names of the image files used by combine filter
    filenames = [
            "red_image.png",
            "green_image.png",
            "blue_image.png"
    ]

    # Take each image filename and load the images into a list
    images = [load_image(filename) for filename in filenames]

    # Show channel filters
    print("Showing images...")

    print("Red channel")
    show(red_channel(image))

    print("Green channel")
    show(green_channel(image))

    print("Blue channel")
    blue_image = blue_channel(image)
    show(blue_image)

    print("Combine filter")
    # Unpack the list of images into combine_filter then show the result
    show(combine_filter(*images))

    print("Done.")
