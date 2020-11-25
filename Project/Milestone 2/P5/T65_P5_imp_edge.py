# Quinn Parrott
# 101169535
# Team 65
from Cimpl import Image, create_color, create_image, get_width, get_height,\
        get_color, set_color
from simple_Cimpl_filters import grayscale

BLACK = create_color(0, 0, 0)
WHITE = create_color(255, 255, 255)


def detect_edges_better(image: Image, threshold: int = 3) -> Image:
    """
    Return an image where each pixels has been compared with its adjacent
    right and bottom pixel. If the contrast of either exceeds the threshold
    the pixel will be black, if not the pixel will be white.

    Author: Quinn Parrott 101169535

    >>> image = load_image(choose_file())
    >>> edge = detect_edges_better(image, threshold=4)
    >>> show(edge)
    """
    # Average all the pixels
    image = grayscale(image)

    # Allocated the edge detected image
    edge_image = create_image(get_width(image), get_height(image))

    # Note: The following 3 loops could be cleaned up into 1 loop but this
    # would negatively impact performance due to the extra if statements.

    # Pass all the interior pixels (excluding bottom and right most pixels)
    for y in range(get_height(image) - 1):
        for x in range(get_width(image) - 1):
            current = get_color(image, x, y)[0]
            bottom = get_color(image, x, y+1)[0]
            right = get_color(image, x+1, y)[0]

            if abs(current - bottom) > threshold or \
               abs(current - right) > threshold:
                set_color(edge_image, x, y, BLACK)
            else:
                set_color(edge_image, x, y, WHITE)

    # Right side
    for y in range(get_height(image) - 1):
        x = get_width(image) - 1

        current = get_color(image, x, y)[0]
        bottom = get_color(image, x, y+1)[0]

        if abs(current - bottom) > threshold:
            set_color(edge_image, x, y, BLACK)
        else:
            set_color(edge_image, x, y, WHITE)

    # Bottom side
    for x in range(get_width(image) - 1):
        y = get_height(image) - 1

        current = get_color(image, x, y)[0]
        right = get_color(image, x+1, y)[0]
        print(f"C{current} r{right} {abs(current - right)} {threshold}")

        if abs(current - right) > threshold:
            set_color(edge_image, x, y, BLACK)
        else:
            set_color(edge_image, x, y, WHITE)

    # Bottom left corner has no neighbors
    set_color(edge_image, get_width(image) - 1, get_height(image) - 1, WHITE)

    return edge_image


if __name__ == '__main__':
    from Cimpl import show, load_image
    for thr in [2, 5, 10, 20]:
        show(
            detect_edges_better(
                load_image("miss_sullivan.jpg"), threshold=thr
            )
        )
