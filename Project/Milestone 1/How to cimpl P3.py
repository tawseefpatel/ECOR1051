from Cimpl import *
filename = "miss_sullivan.jpg"

original_image = load_image(filename)

for pixel in original_image:
    x, y, (r,g,b) = pixel
new_image = copy(original_image)

for pixel in original_image:    
    x, y, (r, g, b) = pixel      
    new_colour = create_color(g,b,r)  
show(original_image)
show(new_image)
