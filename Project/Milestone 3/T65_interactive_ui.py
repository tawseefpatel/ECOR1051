# Milestone 3
# Team 65
# Members:
# -Amelia Hronowsky 101142991
# -Quinn Parrott 101169535
# -Ifeoluwa Shonibare 101164650
# -Tawseef Patel 101145333

from T65_user_interface import execute_command_sequence

HELP_TEXT = (
        "L)oad image\tS)ave_As\n"
        "2)-tone\t3)-tone\tX)treme contrast\tT)int Sepia "
        "\tP)osterize\nE)dge detect\tI)mproved edge detect\tV)ertical "
        "flip\tH)orizontal Flip\nQ)uit\n\n: ")

inputted_task = ""

image = None

while inputted_task != "Q":

    inputted_task = input(HELP_TEXT)
    inputted_task = inputted_task.upper()

    image = execute_command_sequence(image, inputted_task)
