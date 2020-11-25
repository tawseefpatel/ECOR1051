#Author: Amelia Hronowsky
#101142991
#Team 65

from Cimpl import *

def flip_vertical(image: Image) -> Image:
    """Function takes an image and returns a copy of the image that has been flipped vertically (across the "y" axis in an x-y co-ordinate system)
    """
    flipped_image = copy(image)
    middle_pixel = get_width(flipped_image) // 2
    width = get_width(flipped_image)
    height = get_height(flipped_image)
    
    for x in range(middle_pixel):
        for y in range(height):
            r,g,b = get_color(image,x,y)
            new_r, new_g, new_b = get_color(image, abs(width-x) - 1, y)
            set_color(flipped_image,x,y,create_color(new_r,new_g,new_b))
            set_color(flipped_image,width-x-1,y,create_color(r,g,b))
    
    return flipped_image

#Image Loading
if __name__ == "__main__":
    file = load_image(choose_file())
    show(flip_vertical(file))
    
def check_equal(description: str, outcome, expected) -> None:
    """Cehecks if expected value are equal to calculated values.
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
    
def test_flip_vertical() -> None:  
    '''A test function for vertical flip filter. 
    
    Author: Amelia Hronowsky 101142991
    
    >>> test_flip_vertical()
    '''
 
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))  
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 0,  create_color(254, 255, 255))
    set_color(expected, 2, 0,  create_color(125, 73, 224))
    set_color(expected, 3, 0,  create_color(127, 127, 127))
    set_color(expected, 4, 0,  create_color(0, 0, 1))
    set_color(expected, 5, 0,  create_color(0, 0, 0))
       
    
    vertical_image = flip_vertical(original)   
    for x, y, col in vertical_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

test_flip_vertical()