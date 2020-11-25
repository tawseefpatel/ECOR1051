#Ifeoluwa Shonibare 101164650
#Team 65
from Cimpl import *
from simple_Cimpl_filters import grayscale

def sepia_channel(pic: Image) -> Image:
    """Returns a new image with grayscale first applied to each pixel, 
    then the red and blue components are adjusted, leaving the green pixels
    unchanged
    
    >>> sepia(choose_file())
    """
    sepia_image = copy(pic)
    sepia_image = grayscale(sepia_image)
    for pixel in sepia_image:
        x, y, (r, g, b) = pixel
        if r < 63:
            sepia_filter = create_color((r * 1.1), g, (b * 0.9))
            set_color(sepia_image, x, y, sepia_filter)
        elif 63 <= r <= 191:
            sepia_filter = create_color((r * 1.15), g, (b * 0.85))
            set_color(sepia_image, x, y, sepia_filter)
        else:
            sepia_filter = create_color((r * 1.08), g, (b * 0.93))
            set_color(sepia_image, x, y, sepia_filter)            
    return sepia_image

pic = load_image(choose_file())
show(sepia_channel(pic))
