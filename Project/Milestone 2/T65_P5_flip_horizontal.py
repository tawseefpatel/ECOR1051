# Author: Amelia Hronowsky 101142991
# Team 65


from Cimpl import *

def flip_horizontal(image: Image) -> Image:

    """ Returns a original_image after flipping along the x-axis (horizontal flip)
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
            set_color(horizontal_image, x, height - y - 1, create_color(r, g, b))
    
    return horizontal_image


#IMAGE LOADING 
if __name__ == "__main__":
    file = load_image(choose_file())
    show(flip_horizontal(file))   