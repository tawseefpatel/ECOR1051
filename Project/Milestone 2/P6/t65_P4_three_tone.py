from Cimpl import *

'#Created by Tawseef Patel'
'#student number:101145333'
'#Team number 65'


def three_toned(file: Image, colour1: str, colour2: str, colour3: str) -> Image:
    """returns a copy of an image in which there are only three colours/tones.
    If a pixel’s brightness is between 0 and 84, the corresponding pixel in the
    three-tone image is set to the first colour; for example, black. If a
    pixel's brightness is between 85 and 170, the corresponding pixel in the
    three-tone image is set to the second colour; for example, white. If a
    pixel's brightness is between 171 and 255, the corresponding pixel in the
    three-tone image is set to the third colour; for example, gray. """

    #assign colour code number for each colour
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

    if colour1 == "grey":
        colour1 = create_color(128, 128, 128)
    if colour2 == "grey":
        colour2 = create_color(128, 128, 128)
    if colour3 == "grey":
        colour3 = create_color(128, 128, 128)
#------------------------------------------------------------------------------

    copied_image = copy(file)
    for x, y, (r, g, b) in copied_image:
        colors = get_color(copied_image, x, y)
        brightness = sum(colors)/3
        if brightness <= 84:
            three_tone_colors = colour1
            three_tone_copy = copied_image
            three_tone_image = set_color(three_tone_copy, x, y,
                                         three_tone_colors)

        if 84 < brightness <= 170:
            three_tone_colors = colour2
            three_tone_copy = copied_image
            three_tone_image = set_color(three_tone_copy, x, y,
                                         three_tone_colors)

        if 170 < brightness <= 255:
            three_tone_colors = colour3
            three_tone_copy = copied_image
            three_tone_image = set_color(three_tone_copy, x, y,
                                         three_tone_colors)

    return three_tone_copy


'#IMAGE LOADING'
if __name__ == "__main__":
    file = load_image(choose_file())
    show(three_toned(file, "black", "white", "grey"))  #enter 3 colour (black, white, red, blue, lime, yellow, cyan, magenta, grey)
