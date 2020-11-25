#Ifeoluwa Shonibare 101164650
#Team 65
from Cimpl import *

def test_two_tone() -> None:
    """Returns 'PASSED' if pixels from two_tone match with the calculated pixels
    from expected_image
    
    >>> test_two_tone()
    """
    original = create_image(4, 1)
    set_color(original, 0, 0,  create_color(47, 89, 198))
    set_color(original, 1, 0,  create_color(111, 7, 215))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 140, 224))

    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(255, 255, 255))
    set_color(expected, 2, 0,  create_color(0, 0, 0))
    set_color(expected, 3, 0,  create_color(255, 255, 255))
    
    two_tone_image = two_tone_channel(original, "white", "black")   
    for x, y, col in two_tone_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
        
