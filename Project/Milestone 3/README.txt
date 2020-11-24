Photo Editor
_Version 1.0_ 2020-04-07

A program to apply basic filters to an image interactively or in batch from the command line.
Filters include:
- Extreme Contrast
- Posterize
- Sepia
- Two and Three Toned
- Edge Detect
- Improved Edge Detect
- Vertical and Horizontal Flips

This software is licensed under the free open-source MIT License and is therefor free to use, modify and redistribute. See _License_ section for more details.

This project contains the files:
- `T65_batch_ui.py`
- `T65_interactive_ui.py`
- `T65_user_interface.py`
- `T65_image_filters.py`
- `Cimply.py`
- `simple_Cimpl_filters.py`

Contact Quinn Parrott (quinnparrott@cmail.carleton.ca) for more details.

Installation:
-------------
Python 3 is required. This software has been tested with Python 3.7 and 3.8. A version of Pillow/PIL is required. Python's Standard Library is used.

Usage:
------
All commands consist of the first letter (or number) of the filter or command. All commands are case insensitive. A list of commands can be found by running interactive mode.

Interactive:
------------
```
$ python T65_interactive.py
```
A number of filters will be listed along with commands to load and save images. Press `Q` then return to exit.

Batch:
------
A batch version of the filters is possible to use by putting commands and image files into a text file. The format of the file is as such:
```
<source_image_path> <destination_image_path> <commands>
input1.png output1.png X P H
input2.png output2.png V S
```

For batch mode run:
```
$ python T65_batch_ui.py
```
When prompted enter the location of the batch formatted text file.

License:
--------
This software is licensed under the MIT License. MIT is a free and open-source license that is simple and permissive allowing for use, modification and redistribution.
More information at https://choosealicense.com/licenses/mit/.

Credits:
--------
Ifeoluwa Shonibare - Edge Detect, Sepia and Interactive UI
Amelia Hronowsky - Extreme Contrast and Horizontal Flip
Tawseef Patel - 2/3 Toned, Vertical Flip and Batch UI
Quinn Parrott - Better Edge Detect, Posterize and Refactoring of User Interface
Don L. Bailey - Cimpl (Carleton Image Manipulation Python Library)