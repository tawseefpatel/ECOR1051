
from Cimpl import *
from test_invert import check_equal
from simple_Cimpl_filters import grayscale

def sepia_filter(pic: Image) -> Image:
    """Returns a new image with grayscale first applied to each pixel, 
    then the red and blue components are adjusted, leaving the green pixels
    unchanged
    
    Author: Ifeoluwa Shonibare 101164650
    
    >>> sepia(choose_file())
    """
    sepia_image = copy(pic)
    sepia_image = grayscale(sepia_image)
    for pixel in sepia_image:
        x, y, (r, g, b) = pixel
        if r < 63:
            sepia_color = create_color(round(r * 1.1), g, round(b * 0.9))
            set_color(sepia_image, x, y, sepia_color)
        elif 63 <= r <= 191:
            sepia_color = create_color(round(r * 1.15), g, round(b * 0.85))
            set_color(sepia_image, x, y, sepia_color)
        else:
            sepia_color = create_color(round(r * 1.08), g, round(b * 0.93))
            set_color(sepia_image, x, y, sepia_color)            
    return sepia_image

if __name__ == "__main__":
    pic = load_image(choose_file())
    show(sepia_filter(pic))