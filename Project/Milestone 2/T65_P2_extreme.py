# Author: Amelia Hronowsky 101142991 Team 65

from Cimpl import *

def extreme_contrast (image: Image) -> Image:
    """Returns an extreme contrast copied version of the original image.
    
    >>>image = load_image(choose_file())
    >>>extreme_image = extreme_contrast(image)
    >>>show (extreme_image)
    
    """
    new_image = copy (image)
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
        set_color (new_image, x, y, extreme)
    return new_image

image = load_image(choose_file())
extreme_image = extreme_contrast(image)
show(extreme_image)
