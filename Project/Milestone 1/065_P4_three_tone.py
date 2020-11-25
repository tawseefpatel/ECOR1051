#Ifeoluwa Shonibare 101164650
#Team 65
from Cimpl import *

def test_three_tone() -> None:
    """Returns 'PASSED' if pixels from three_tone match with the calculated pixels
    from expected_image
    
    >>> test_two_tone()
    """
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(47, 3, 66))
    set_color(original, 1, 0,  create_color(120, 33, 175))
    set_color(original, 2, 0,  create_color(201, 227, 186))
    set_color(original, 3, 0,  create_color(125, 140, 224))
    set_color(original, 3, 0,  create_color(187, 140, 77))
    set_color(original, 3, 0,  create_color(111, 14, 66))

    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(255, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 255, 0))
    set_color(expected, 2, 0,  create_color(0, 0, 255))
    set_color(expected, 3, 0,  create_color(0, 255, 0))
    set_color(expected, 3, 0,  create_color(0, 255, 0))
    set_color(expected, 3, 0,  create_color(255, 0, 0)) 
    
    three_tone_image = three_tone_channel(original, "red", "lime", "blue")   
    for x, y, col in three_tone_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
