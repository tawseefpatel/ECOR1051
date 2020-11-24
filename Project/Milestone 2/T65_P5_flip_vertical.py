from Cimpl import *

'#Created by Tawseef Patel 101145333'
'#Team Number 65'


def flip_vertical(image: Image) -> Image:
    """Function takes an image and returns a copy of the image that has been
    flipped vertically (across the "y" axis in an x-y co-ordinate system)
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

'#IMAGE LOADING'
if __name__ == "__main__":
    file = load_image(choose_file())
    show(flip_vertical(file))
