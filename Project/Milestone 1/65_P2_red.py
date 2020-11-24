#Created by Tawseef Patel
#student number:101145333
#Team number 65


from Cimpl import choose_file, load_image, copy, create_color, set_color, show, Image, get_color, create_image

image1 = load_image("miss_sullivan.jpg")

def red_channel(file: Image)-> Image:
    """Returns the selected file with no G or B values. (Returns the file with only red pixels) """
    original_image = copy(file)
    for x, y, (r, g, b) in original_image:
        red_color = create_color(r, g-g, b-b)
        red_image = original_image
        colors = set_color(red_image, x,y, red_color) 

    return red_image

show(red_channel(image1))

def check_equal(description: str, outcome, expected) -> None:
    """
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        print("{0} FAILED: expected({1}) has type {2}," \
              "but outcome ({3}) has type {4}". 
              formal(description, expected, str(expected_type).strip('<class>'), outcome, str(outcome_type).strip('<class.')))
    elif outcome != expected:
        print(("{0} FAILED: expected {1}, got {2}".
               format(description, expected, outcome)))
    else:
        print("{0} PASSED".format(description))
    print("---------------------------------------------------------------------")

def test_red()-> None:
    """Checks if the G and B pixels are equal to 0 and only red is present
    >>>test_red(red_channel(image1))
    >>>Filter has Passed
    """
    original = create_image(6,1)
    set_color(original, 0, 0, create_color(0,0,0))
    set_color(original, 1, 0, create_color(1,0,0))
    set_color(original, 2, 0, create_color(127,127,127))
    set_color(original, 3, 0, create_color(125,73,224))
    set_color(original, 4, 0, create_color(254,255,255))
    set_color(original, 5, 0, create_color(255,255,255))
    
    expected = create_image(6,1)
    set_color(expected, 0, 0, create_color(0,0,0))
    set_color(expected, 1, 0, create_color(1,0,0))
    set_color(expected, 2, 0, create_color(127,0,0))
    set_color(expected, 3, 0, create_color(125,0,0))
    set_color(expected, 4, 0, create_color(254,0,0))
    set_color(expected, 5, 0, create_color(255,0,0))
    
    red = red_channel(original)
    for x, y, col in red:
        check_equal('Checking pixel @(' + str(x) + ','+ str(y) + ')', col, get_color(expected, x,y))

test_red()