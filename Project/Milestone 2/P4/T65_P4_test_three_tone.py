
from Cimpl import *
from test_invert import check_equal
from t65_P4_three_tone import three_toned

def test_three_tone() -> None:
    """Returns 'PASSED' if pixels from three_tone match with the calculated pixels
    from expected_image
    
    Author: Ifeoluwa Shonibare 101164650
    
    >>> test_three_tone()
    """
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(47, 3, 66))
    set_color(original, 1, 0,  create_color(120, 33, 175))
    set_color(original, 2, 0,  create_color(201, 227, 186))

    expected_1 = create_image(3, 1)
    set_color(expected_1, 0, 0,  create_color(0, 0, 0))
    set_color(expected_1, 1, 0,  create_color(255, 255, 255))
    set_color(expected_1, 2, 0,  create_color(255, 0, 0))
    
    three_tone_image = three_tone(original, "black", "white", "red")   
    for x, y, col in three_tone_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_1, x, y))
        
    expected_2 = create_image(3, 1)
    set_color(expected_2, 0, 0,  create_color(0, 255, 0))
    set_color(expected_2, 1, 0,  create_color(0, 0, 255))
    set_color(expected_2, 2, 0,  create_color(255, 255, 0))
    
    three_tone_image = three_toned(original, "lime", "blue", "yellow")   
    for x, y, col in three_tone_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_2, x, y))
    
    expected_3 = create_image(3, 1)
    set_color(expected_3, 0, 0,  create_color(0, 255, 255))
    set_color(expected_3, 1, 0,  create_color(255, 0, 255))
    set_color(expected_3, 2, 0,  create_color(128, 128, 128))
    
    three_tone_image = three_toned(original, "cyan", "magenta", "gray")   
    for x, y, col in three_tone_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_3, x, y))

test_three_tone()