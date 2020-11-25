# Author: Amelia Hronowsky 101142991

from Cimpl import choose_file, load_image, copy, create_color, set_color, \
     show, Image, get_color, create_image

def blue_channel(image: Image) -> Image:
    """Returns a copy of the original image with a blue filter, with zero green and red pixel componets.
    
    >>>image = load_image(choose_file())
    >>>blue_image = blue_channel(image)
    >>>show(blue_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        r, g, b = 0, 0, b
        blue = create_color(r, g, b)
        set_color(new_image, x, y, blue)
    return new_image

image = load_image(choose_file())
blue_image = blue_channel(image)
show(blue_image)

def check_equal(description: str, outcome, expected) -> None:
    """
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")
    
def test_blue_channel() -> None:  
    '''A test function for blue filter. Returns PASSED if no pixel components 
    are red and green and failed otherwsie.
    
    >>> test_blue_channel()
    '''
 
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))  
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 1))
    set_color(expected, 2, 0,  create_color(0, 0, 127))
    set_color(expected, 3, 0,  create_color(0, 0, 224))
    set_color(expected, 4, 0,  create_color(0, 0, 255))
    set_color(expected, 5, 0,  create_color(0, 0, 255))
       
    
    blue = blue_channel(original)   
    for x, y, col in blue: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
test_blue_channel()