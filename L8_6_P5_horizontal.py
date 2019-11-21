from Cimpl import *

file = choose_file()
image = load_image(file)

def flip_horizontal(image: Image) -> Image:
    """
    Return the image flipped vertically
    
    >>> image = load_image(choose_file())
    >>> flip_vertical(image)    
    """
    centre_h = get_height(image)//2
    w = get_width(image)
    h = get_height(image)
    for x in range(w):
        for y in range(centre_h):
            r, g, b = get_color(image,x,y)
            r2, g2, b2 = get_color(image,x, h-y-1)
            set_color(image, x, y, create_color(r2,g2,b2))
            set_color(image, x, h-y-1, create_color(r,g,b))
            
    show(image)
    return image

copy = flip_horizontal(image)