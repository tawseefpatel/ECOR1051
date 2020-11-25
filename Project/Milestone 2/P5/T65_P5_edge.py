from Cimpl import *

def detect_edges(image: Image, threshold: int) -> Image:
    """Returns an image that looks like a pencil sketch, by changing the pixels'
    colours to black or white
    
    Author: Ifeoluwa Shonibare 101164650
    
    detect_edges(load_image(choose_file()), 1)
    """
    edge_pic = copy(image)
    height = get_height(edge_pic)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    for pixel in edge_pic:
        x, y, (r, g, b) = pixel      
        if y == (height - 1):
            set_color(edge_pic, x, y, white)
        else:
            r_top, g_top, b_top = get_color(edge_pic, x, y)
            r_bottom, g_bottom, b_bottom = get_color(edge_pic, x, (y + 1))
            top_brightness = (r_top + g_top + b_top) // 3
            bottom_brightness = (r_bottom + g_bottom + b_bottom) // 3
            contrast = abs(top_brightness - bottom_brightness)
            if contrast > threshold:
                set_color(edge_pic, x, y, black)
            else:
                set_color(edge_pic, x, y, white)
    return edge_pic


if __name__ == "__main__":
    result = load_image('miss_sullivan.jpg')
    for thr in [1, 2, 3, 4, 5]:
        print(f"Threshold: {thr}")
        show(detect_edges(result, thr))