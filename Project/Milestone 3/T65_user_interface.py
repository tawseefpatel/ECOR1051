# Milestone 3
# Team 65
# Members:
# -Amelia Hronowsky 101142991
# -Quinn Parrott 101169535
# -Ifeoluwa Shonibare 101164650
# -Tawseef Patel 101145333

from Cimpl import Image, load_image, choose_file, save_as, show
from T65_image_filters import two_toned, three_toned, extreme_contrast,\
    sepia_filter, posterize_filter, detect_edges, detect_edges_better,\
    flip_vertical, flip_horizontal


def execute_command_sequence(
        image: Image, commands: str, is_batch: bool = False
        ) -> Image:
    """
    Execute a series of commands on an image. Supports arguments to the
    filters.

    >>> execute_command_sequence(load_image(choose_file()), "X 2(yellow,cyan) C P")
    """
    # Separate each command, commands are separated by a space
    for command_str in commands.split(" "):

        # Decides if there are arguments in the form of
        # "A(argument1,argument2)"
        # Since the code splits a '(' if there are two elements after the split
        # then there are arguments and if not there are no arguments
        pre_args = command_str.split("(")
        if len(pre_args) > 1:
            # Since there was more than one element this must have arguments

            # Separate the command from the arguments
            command, pre_args = pre_args
            # Separate the command arguments
            pre_args = pre_args.split(",")

            # Preform some cleanup on each argument
            args = []
            for arg in pre_args:
                # Remove some characters that are invalid
                arg = arg.strip("()\"'")
                # If the argument is a number convert it to a number
                if arg.replace(".", "", 1).isdigit():
                    arg = float(arg)

                args.append(arg)
        else:
            # Only one element, the command. No arguments
            command = pre_args[0]
            args = []

        # To ignore the case of the command
        command = command.upper()

        # Execute
        image = execute_command(image, command, args, is_batch)

    return image


def execute_command(
        image: Image, command: str, command_arguments: [str] = [],
        is_batch: bool = False
        ) -> Image:
    """
    Execute a single command on an image.

    >>> image = load_image(choose_file())
    >>> execute_command(image, "X")
    >>> execute_command(image, "X", ["yellow", "cyan", "magenta"])
    """
    # These load command. This command is separate from the
    # filters so that "no image" is not printed if it is used
    if command == "L":
        if len(command_arguments) == 1:
            image = load_image(command_arguments[0])
        else:
            image = load_image(choose_file())
        return image

    # "command in ..." is checked so that if the command does
    # not exist "No image" will not be printed
    if not image and command in "A23XSPEIVH":
        print("No image")
        return  # Skip the rest of the function because no image

    # Call filters when given a command
    if command == "S":
        if len(command_arguments) == 1:
            image = load_image(command_arguments[0])
        else:
            filename = input(
                "Input the filename with file extension "
                "(e.g. new_image.jpg): ")
        save_as(image, filename)
        return image
    elif command == "2":
        if len(command_arguments) == 2:
            # *variable notation is called argument packing and unpacking
            image = two_toned(image, *command_arguments)
        else:
            image = two_toned(
                image,
                "yellow", "cyan"
            )

    elif command == "3":
        if len(command_arguments) == 3:
            image = three_toned(image, *command_arguments)
        else:
            image = three_toned(
                image,
                "yellow", "magenta", "cyan"
            )

    elif command == "X":
        image = extreme_contrast(image, *command_arguments)

    elif command == "T":
        image = sepia_filter(image, *command_arguments)

    elif command == "P":
        image = posterize_filter(image, *command_arguments)

    elif command == "E":
        if len(command_arguments) == 1:
            image = detect_edges(image, *command_arguments)
        else:
            if is_batch:
                image = detect_edges(image, 10)
            else:
                image = detect_edges(
                    image,
                    int(input("Threshold?: "))
                )

    elif command == "I":
        if len(command_arguments) == 1:
            image = detect_edges_better(image, *command_arguments)
        else:
            if is_batch:
                image = detect_edges_better(image, 10)
            else:
                image = detect_edges_better(
                    image,
                    int(input("Threshold?: "))
                )

    elif command == "V":
        image = flip_vertical(image, *command_arguments)

    elif command == "H":
        image = flip_horizontal(image, *command_arguments)

    else:
        print("No such command")

    if not is_batch and image:
        show(image)

    return image


if __name__ == "__main__":
    inputted_task = ""

    image = None

    while inputted_task != "Q":

        inputted_task = input(
            "L)oad image\tSave)as\n2)-tone\t3)-tone\tX)treme contrast\tS)epia "
            "\tP)osterize\nE)dge detect\tI)mproved edge detect\tV)ertical "
            "flip\tH)orizontal Flip\nQ)uit\n\n: ")

        inputted_task = inputted_task.upper()
