#Ifeoluwa Shonibare 101164650
#Team 65
from Cimpl import *
from test_grayscale import check_equal

PICTURE = load_image('p2-original.jpg')

def green_channel(image: object) -> object:
    """Returns image with a green filter applied by changing every red and 
    blue RGB value to 0 in each pixel
    
    """
    GREEN_PIC = copy(image)
    for pixel in GREEN_PIC:
        x, y, (r, g, b) = pixel
        green_color = create_color(0, g, 0)
        set_color(GREEN_PIC, x, y, green_color)
    return GREEN_PIC

def test_green_channel() -> None:  
    '''Returns 'PASSED' if pixels from green_channel 
    change the original pixels to the expected pixels
    
    '''
    
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

green_result = green_channel(load_image('p2-original.jpg'))
show(green_result)
test_green_channel()
