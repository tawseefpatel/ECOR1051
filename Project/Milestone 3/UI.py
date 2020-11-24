# Team 65
# Members:
# -Amelia Hronowsky 101142991
# -Quinn Parrott 101169535
# -Ifeoluwa Shonibare 101145333
# -Tawseef Patel 101145333

from Cimpl import *
from T65_image_filters import *

inputted_task = ""

image = None

while inputted_task != "Q":

     inputted_task = input(
     
         "L)oad image\tSave)as\n2)-tone\t3)-tone\tX)treme contrast\tS)epia "
     
         "\tP)osterize\nE)dge detect\tI)mproved edge detect\tV)ertical "
     
         "flip\tH)orizontal Flip\nQ)uit\n\n: ")
     
     inputted_task = inputted_task.upper()
     
     if inputted_task == "L":
          image = load_image(choose_file())
          show(image)

     elif inputted_task == "2":
          if image is not None:
               image = two_toned(image, "yellow", "cyan") #we can make this more interactive by allowing the user to pick from a set of colours, so if 2 is clicked then it sets open another ui that requires the user to seelect from a range of colours that the code is set to have
               show(image)
          print("No image loaded.")

     elif inputted_task == "3":
          if image is not None:
               image = three_toned(image, "yellow", "magenta", "cyan") #I think we can make this more interactive like the 2 tone
               show(image)     
          print("No image loaded.")

     elif inputted_task == "X":
          if image is not None:
               image = extreme_contrast(image)
               show(image)
          print("No image loaded")
   
     elif inputted_task == "S":
          if image is not None:
               image = sepia_filter(image) 
               show(image) 
          print("No image loaded")
     
     elif inputted_task == "P":
          if image is not None:
               image = posterize_filter(image)
     
               show(image)
          print("No image loaded")

     elif inputted_task == "E":
          if image is not None:
               threshold = float(input("Input a threshold value: "))
               image = detect_edges(image, threshold)
               show(image)
          print("No image loaded")

     elif inputted_task == "I": #I edited the image_filters code because there were a bunch of values that kept printing when this filter was used, i commented out the print line in the code for myself, be sure to do that in the good copy
          if image is not None:
               threshold = float(input("Input a threshold value: "))
               image = detect_edges_better(image, threshold)
               show(image)
          print("No image loaded")

     elif inputted_task == "V":
          if image is not None:
               image = flip_vertical(image)
               show(image)
          print("No image loaded")

     elif inputted_task == "H":
          if image is not None:
               image = flip_horizontal(image)
               show(image)
          print("No image loaded")

     elif inputted_task == "Save":
          if image is not None:
               filename = input(
                    "Input the filename with file extension "
                    "(e.g. new_image.jpg): ")
               print("test")
               show(image)
               save_as(image, filename)
          print("No image loaded")

     elif inputted_task == "Q":
          pass    
     else:
          print("No such command")        