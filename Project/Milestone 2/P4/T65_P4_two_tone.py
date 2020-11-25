#Created by Tawseef Patel
#student number:101145333
#Team number 65

from Cimpl import *


def two_toned(file: Image, colour1:str, colour2:str)-> Image:
    """ returns a copy of an image in which there are only two colours (tones). If a pixel’s brightness is between 0 and 127, the corresponding pixel in the two-tone image is set to the first colour; for example, black. If a pixel's brightness is between 128 and 255, the corresponding pixel in the two-tone image is set to the second colour; for example, white"""
    
    #assign colour code number for each colour
    if colour1 == "black": colour1 = create_color(0,0,0)
    if colour2 == "black": colour2 = create_color(0,0,0)
    
    if colour1 == "white": colour1 = create_color(255,255,255)
    if colour2 == "white": colour2 = create_color(255,255,255)
        
    if colour1 == "red": colour1 = create_color(255,0,0)
    if colour2 == "red": colour2 = create_color(255,0,0)    
        
    if colour1 == "lime": colour1 = create_color(0,255,0)
    if colour2 == "lime": colour2 = create_color(0,255,0)
        
    if colour1 == "blue": colour1 = create_color(0,0,255)
    if colour2 == "blue": colour2 = create_color(0,0,255) 
        
    if colour1 == "yellow": colour1 = create_color(255,255,0)
    if colour2 == "yellow": colour2 = create_color(255,255,0) 
        
    if colour1 == "cyan": colour1 = create_color(0,255,255)
    if colour2 == "cyan": colour2 = create_color(0,255,255) 
    
    if colour1 == "magenta": colour1 = create_color(255,0,255)
    if colour2 == "magenta": colour2 = create_color(255,0,255)   
        
    if colour1 == "grey": colour1 = create_color(128,128,128)
    if colour2 == "grey": colour2 = create_color(128,128,128)     
#-------------------------------------------------------------------------------    
    
   
    copied_image = copy(file)         
    for x,y, (r,g,b) in copied_image:
        colors = get_color(copied_image, x,y) 
        average = sum(colors)/3
        if average < 127:
            two_tone_colors = colour1
            two_tone_copy = copied_image
            two_tone_image = set_color(two_tone_copy, x,y, two_tone_colors)
            
        else:
            two_tone_colors = colour2
            two_tone_copy = copied_image
            two_tone_image = set_color(two_tone_copy, x,y, two_tone_colors)      
       
    return two_tone_copy




#IMAGE LOADING 
if __name__ == "__main__":
    file = load_image(choose_file())
    show(two_toned(file, "black", "white")) #enter a colour (black, white, red, blue, lime, yellow, cyan, magenta, grey)