# Team 65
# Members:
# -Amelia Hronowsky 101142991
# -Quinn Parrott 101169535
# -Ifeoluwa Shonibare 101145333
# -Tawseef Patel 101145333

from Cimpl import Image, create_image, get_width, get_height,\
    copy, Color, create_color, set_color, get_color
from simple_Cimpl_filters import grayscale


BLACK = create_color(0, 0, 0)
WHITE = create_color(255, 255, 255)


def red_channel(file: Image) -> Image:
    """
    Returns the image with no G or B values

    Author: Tawseef Patel 101145333
    """
    original_image = copy(file)
    for x, y, (r, g, b) in original_image:
        red_color = create_color(r, g-g, b-b)
        red_image = original_image
        set_color(red_image, x, y, red_color)

    return red_image


def green_channel(image: Image) -> Image:
    """
    Returns image with a green filter applied by changing every red and
    blue RGB value to 0 in each pixel

    Author: Ifeoluwa Shonibare 101145333

    >>> green_image = green_channel(load_image(choose_file()))
    >>> show(green_image)
    """
    green_pic = copy(image)
    for x, y, (_, g, _) in green_pic:
        green_color = create_color(0, g, 0)
        set_color(green_pic, x, y, green_color)
    return green_pic


def blue_channel(image: Image) -> Image:
    """
    Returns a copy of the original image with a blue filter, with zero green
    and red pixel components.

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


def combine_filter(
        red_channel: Image, green_channel: Image, blue_channel: Image
        ) -> Image:
    """
    Return an Image that is a combination of red, green and blue channel of
    three other images.

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
    combined_image = create_image(
        get_width(red_channel),
        get_height(red_channel)
    )

    for x, y, _ in combined_image:
        # Get the color from each channel
        red_color = get_color(red_channel, x, y)
        green_color = get_color(green_channel, x, y)
        blue_color = get_color(blue_channel, x, y)

        # Combining the colors together
        combined_color = Color(red_color[0], green_color[1], blue_color[2])

        set_color(combined_image, x, y, combined_color)

    return combined_image


def extreme_contrast(image: Image) -> Image:
    """
    Returns an extreme contrast copied version of the original image.

    Author: Amelia Hronowsky 101142991

    >>>image = load_image(choose_file())
    >>>extreme_image = extreme_contrast(image)
    >>>show (extreme_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        if r < 128:
            red = create_color(0, g, b)
        else:
            red = create_color(255, g, b)
        if g < 128:
            green = create_color(r, 0, b)
        else:
            green = create_color(r, 255, b)
        if b < 128:
            blue = create_color(r, g, 0)
        else:
            blue = create_color(r, g, 255)

        r, g, b = red, green, blue
        extreme = create_color(r[0], g[1], b[2])
        set_color(new_image, x, y, extreme)
    return new_image


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


def sepia_filter(pic: Image) -> Image:
    """Returns a new image with grayscale first applied to each pixel,
    then the red and blue components are adjusted, leaving the green pixels
    unchanged

    Author: Ifeoluwa Shonibare 101164650

    >>> sepia(choose_file())
    """
    sepia_image = grayscale(copy(pic))
    for pixel in sepia_image:
        x, y, (r, g, b) = pixel
        if r < 63:
            sepia_color = create_color(round(r * 1.1), g, round(b * 0.9))
        elif 63 <= r <= 191:
            sepia_color = create_color(round(r * 1.15), g, round(b * 0.85))
        else:
            sepia_color = create_color(round(r * 1.08), g, round(b * 0.93))
        set_color(sepia_image, x, y, sepia_color)
    return sepia_image


def three_toned(
        file: Image, colour1: str, colour2: str, colour3: str
        ) -> Image:
    """
    Returns a copy of an image in which there are only three colours/tones.
    If a pixel's brightness is between 0 and 84, the corresponding pixel in the
    three-tone image is set to the first colour; for example, black. If a
    pixel's brightness is between 85 and 170, the corresponding pixel in the
    three-tone image is set to the second colour; for example, white. If a
    pixel's brightness is between 171 and 255, the corresponding pixel in the
    three-tone image is set to the third colour; for example, gray.

    Author: Tawseef Patel 101145333
    """

    # assign colour code number for each colour
    if colour1 == "black":
        colour1 = create_color(0, 0, 0)
    if colour2 == "black":
        colour2 = create_color(0, 0, 0)
    if colour3 == "black":
        colour3 = create_color(0, 0, 0)

    if colour1 == "white":
        colour1 = create_color(255, 255, 255)
    if colour2 == "white":
        colour2 = create_color(255, 255, 255)
    if colour3 == "white":
        colour3 = create_color(255, 255, 255)

    if colour1 == "red":
        colour1 = create_color(255, 0, 0)
    if colour2 == "red":
        colour2 = create_color(255, 0, 0)
    if colour3 == "red":
        colour3 = create_color(255, 0, 0)

    if colour1 == "lime":
        colour1 = create_color(0, 255, 0)
    if colour2 == "lime":
        colour2 = create_color(0, 255, 0)
    if colour3 == "lime":
        colour3 = create_color(0, 255, 0)

    if colour1 == "blue":
        colour1 = create_color(0, 0, 255)
    if colour2 == "blue":
        colour2 = create_color(0, 0, 255)
    if colour3 == "blue":
        colour3 = create_color(0, 0, 255)

    if colour1 == "yellow":
        colour1 = create_color(255, 255, 0)
    if colour2 == "yellow":
        colour2 = create_color(255, 255, 0)
    if colour3 == "yellow":
        colour3 = create_color(255, 255, 0)

    if colour1 == "cyan":
        colour1 = create_color(0, 255, 255)
    if colour2 == "cyan":
        colour2 = create_color(0, 255, 255)
    if colour3 == "cyan":
        colour3 = create_color(0, 255, 255)

    if colour1 == "magenta":
        colour1 = create_color(255, 0, 255)
    if colour2 == "magenta":
        colour2 = create_color(255, 0, 255)
    if colour3 == "magenta":
        colour3 = create_color(255, 0, 255)

    if colour1 == "grey" or colour1 == "gray":
        colour1 = create_color(128, 128, 128)
    if colour2 == "grey" or colour2 == "gray":
        colour2 = create_color(128, 128, 128)
    if colour3 == "grey" or colour3 == "gray":
        colour3 = create_color(128, 128, 128)

    copied_image = copy(file)
    for x, y, _ in copied_image:
        colors = get_color(copied_image, x, y)
        brightness = sum(colors)/3
        if brightness <= 84:
            three_tone_colors = colour1
            three_tone_copy = copied_image
            set_color(three_tone_copy, x, y, three_tone_colors)

        if 84 < brightness <= 170:
            three_tone_colors = colour2
            three_tone_copy = copied_image
            set_color(three_tone_copy, x, y, three_tone_colors)

        if 170 < brightness <= 255:
            three_tone_colors = colour3
            three_tone_copy = copied_image
            set_color(three_tone_copy, x, y, three_tone_colors)

    return three_tone_copy


def two_toned(file: Image, colour1: str, colour2: str) -> Image:
    """
    Returns a copy of an image in which there are only two colours (tones).
    If a pixel's brightness is between 0 and 127, the corresponding pixel in
    the two-tone image is set to the first colour; for example, black. If a
    pixel's brightness is between 128 and 255, the corresponding pixel in the
    two-tone image is set to the second colour; for example, white

    Author: Tawseef Patel 101145333
    """

    # assign colour code number for each colour
    if colour1 == "black":
        colour1 = create_color(0, 0, 0)
    if colour2 == "black":
        colour2 = create_color(0, 0, 0)

    if colour1 == "white":
        colour1 = create_color(255, 255, 255)
    if colour2 == "white":
        colour2 = create_color(255, 255, 255)

    if colour1 == "red":
        colour1 = create_color(255, 0, 0)
    if colour2 == "red":
        colour2 = create_color(255, 0, 0)

    if colour1 == "lime":
        colour1 = create_color(0, 255, 0)
    if colour2 == "lime":
        colour2 = create_color(0, 255, 0)

    if colour1 == "blue":
        colour1 = create_color(0, 0, 255)
    if colour2 == "blue":
        colour2 = create_color(0, 0, 255)

    if colour1 == "yellow":
        colour1 = create_color(255, 255, 0)
    if colour2 == "yellow":
        colour2 = create_color(255, 255, 0)

    if colour1 == "cyan":
        colour1 = create_color(0, 255, 255)
    if colour2 == "cyan":
        colour2 = create_color(0, 255, 255)

    if colour1 == "magenta":
        colour1 = create_color(255, 0, 255)
    if colour2 == "magenta":
        colour2 = create_color(255, 0, 255)

    if colour1 == "grey":
        colour1 = create_color(128, 128, 128)
    if colour2 == "grey":
        colour2 = create_color(128, 128, 128)

    copied_image = copy(file)
    for x, y, _ in copied_image:
        colors = get_color(copied_image, x, y)
        average = sum(colors)/3
        if average < 127:
            two_tone_colors = colour1
            two_tone_copy = copied_image
            set_color(two_tone_copy, x, y, two_tone_colors)

        else:
            two_tone_colors = colour2
            two_tone_copy = copied_image
            set_color(two_tone_copy, x, y, two_tone_colors)

    return two_tone_copy


def detect_edges(image: Image, threshold: int) -> Image:
    """
    Returns an image that looks like a pencil sketch, by changing the pixels'
    colours to black or white

    Author: Ifeoluwa Shonibare 101164650

    >>> detect_edges(load_image(choose_file()), 1)
    """
    edge_pic = grayscale(copy(image))
    height = get_height(edge_pic)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    for pixel in edge_pic:
        x, y, _ = pixel
        if y == (height - 1):
            set_color(edge_pic, x, y, white)
        else:
            top_brightness, _, _ = get_color(edge_pic, x, y)
            bottom_brightness, _, _ = get_color(edge_pic, x, (y + 1))
            contrast = abs(top_brightness - bottom_brightness)
            if contrast > threshold:
                set_color(edge_pic, x, y, black)
            else:
                set_color(edge_pic, x, y, white)
    return edge_pic


def flip_horizontal(image: Image) -> Image:
    """
    Returns a copy of an image after it has been flipped along the
    x axis (horizontal flip).

    Author: Amelia Hronowsky

    >>> show(flip_horizontal(file))
    """
    horizontal_image = copy(image)
    width = get_width(horizontal_image)
    height = get_height(horizontal_image)
    center = height // 2

    for x in range(width):
        for y in range(center):
            r, g, b = get_color(horizontal_image, x, y)
            r2, g2, b2 = get_color(horizontal_image, x, height - y - 1)
            set_color(horizontal_image, x, y, create_color(r2, g2, b2))
            set_color(
                horizontal_image, x, height - y - 1, create_color(r, g, b))

    return horizontal_image


def flip_vertical(image: Image) -> Image:
    """
    Function takes an image and returns a copy of the image that has been
    flipped vertically (across the "y" axis in an x-y co-ordinate system)

    Author: Tawseef Patel 101145333
    """
    flipped_image = copy(image)
    middle_pixel = get_width(flipped_image) // 2
    width = get_width(flipped_image)
    height = get_height(flipped_image)

    for x in range(middle_pixel):
        for y in range(height):
            r, g, b = get_color(image, x, y)
            new_r, new_g, new_b = get_color(image, abs(width - x) - 1, y)
            set_color(flipped_image, x, y, create_color(new_r, new_g, new_b))
            set_color(flipped_image, width - x - 1, y, create_color(r, g, b))

    return flipped_image


def detect_edges_better(image: Image, threshold: int = 3) -> Image:
    """
    Return an image where each pixels has been compared with its adjacent
    right and bottom pixel. If the contrast of either exceeds the threshold
    the pixel will be black, if not the pixel will be white.

    Author: Quinn Parrott 101169535

    >>> image = load_image(choose_file())
    >>> edge = detect_edges_better(image, threshold=4)
    >>> show(edge)
    """
    # Average all the pixels
    image = grayscale(image)

    # Allocated the edge detected image
    edge_image = create_image(get_width(image), get_height(image))

    # Note: The following 3 loops could be cleaned up into 1 loop but this
    # would negatively impact performance due to the extra if statements.

    # Pass all the interior pixels (excluding bottom and right most pixels)
    for y in range(get_height(image) - 1):
        for x in range(get_width(image) - 1):
            current = get_color(image, x, y)[0]
            bottom = get_color(image, x, y+1)[0]
            right = get_color(image, x+1, y)[0]

            if abs(current - bottom) > threshold or \
               abs(current - right) > threshold:
                set_color(edge_image, x, y, BLACK)
            else:
                set_color(edge_image, x, y, WHITE)

    # Right side
    for y in range(get_height(image) - 1):
        x = get_width(image) - 1

        current = get_color(image, x, y)[0]
        bottom = get_color(image, x, y+1)[0]

        if abs(current - bottom) > threshold:
            set_color(edge_image, x, y, BLACK)
        else:
            set_color(edge_image, x, y, WHITE)

    # Bottom side
    for x in range(get_width(image) - 1):
        y = get_height(image) - 1

        current = get_color(image, x, y)[0]
        right = get_color(image, x+1, y)[0]
        print(f"C{current} r{right} {abs(current - right)} {threshold}")

        if abs(current - right) > threshold:
            set_color(edge_image, x, y, BLACK)
        else:
            set_color(edge_image, x, y, WHITE)

    # Bottom left corner has no neighbors
    set_color(edge_image, get_width(image) - 1, get_height(image) - 1, WHITE)

    return edge_image
