
from Cimpl import *
from test_invert import check_equal
from t65_P4_two_tone import two_toned

def test_two_tone() -> None:
    """Returns 'PASSED' if pixels from two_tone match with the calculated pixels
    from expected_image
    
    Author: Ifeoluwa Shonibare 101164650
    
    >>> test_two_tone()
    """
    original = create_image(2, 1)
    set_color(original, 0, 0,  create_color(47, 89, 198))
    set_color(original, 1, 0,  create_color(111, 77, 215))

    expected_1 = create_image(2, 1)
    set_color(expected_1, 0, 0,  create_color(255, 255, 255))
    set_color(expected_1, 1, 0,  create_color(0, 0, 0))
    
    two_tone_image = two_toned(original, "white", "black")   
    for x, y, col in two_tone_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_1, x, y))
   
    expected_2 = create_image(2, 1)
    set_color(expected_2, 0, 0,  create_color(255, 0, 0))
    set_color(expected_2, 1, 0,  create_color(0, 255, 0))   
    
    two_tone_image = two_toned(original, "red", "lime")   
    for x, y, col in two_tone_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_2, x, y))  
    
    expected_3 = create_image(2, 1)
    set_color(expected_3, 0, 0,  create_color(0, 0, 255))
    set_color(expected_3, 1, 0,  create_color(255, 255, 0))   
    
    two_tone_image = two_toned(original, "blue", "yellow")   
    for x, y, col in two_tone_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_3, x, y))  
    
    expected_4 = create_image(2, 1)
    set_color(expected_4, 0, 0,  create_color(0, 255, 255))
    set_color(expected_4, 1, 0,  create_color(255, 0, 255))   
    
    two_tone_image = two_toned(original, "cyan", "magenta")   
    for x, y, col in two_tone_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_4, x, y)) 

test_two_tone()