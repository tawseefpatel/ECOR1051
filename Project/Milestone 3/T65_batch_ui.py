# Milestone 3
# Team 65
# Members:
# -Amelia Hronowsky 101142991
# -Quinn Parrott 101169535
# -Ifeoluwa Shonibare 101164650
# -Tawseef Patel 101145333

from Cimpl import load_image, save_as
from T65_user_interface import execute_command_sequence

file_name = open(input('Please type the name of the batch file: '))

for line in file_name:
    # The second argument of split specifies when to stop spliting the string
    # more specifically all spaces after the first 2 are ignored
    in_path, out_path, command_seq = line.split(" ", 2)

    # Each line of a file ends with a newline and sometimes whitespace,
    # remove it
    command_seq = command_seq.strip("\n ")

    image = load_image(in_path)

    # Execute a sequence of filters commands on an image
    image = execute_command_sequence(image, command_seq, is_batch=True)

    save_as(image, out_path)

file_name.close()
