# L8-6, Milestone 2, November 22nd, 2019

from Cimpl import *

def flip_vertical(image: Image) -> Image:
    """Returns an image that has been flipped through the vertical axis
   
    _Author_ = Jackie So (101153622)
   
    >>>image = load_image(choose_file())
    >>>flip_vertical(image)
    """
   

    flipped_image = copy(image)
    width = get_width(image)
   
    for y in range(get_height(flipped_image)):
        for x in range(get_width(flipped_image)):
            new_color = get_color(image, width - y - 1, y)
            set_color(flipped_image, width - y- 1, y, new_color)
           
    show(flipped_image)    
    return flipped_image

