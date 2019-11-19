from Cimpl import *

file = choose_file()
image = load_image(file)

def detect_edges(image: Image,threshold: int) -> Image:
    """
    Author: Dhriti Aravind
    Return a copy of the image with the edges of the image outlined. 
    
    Preconditions:
    threshold value must be a real postive integer
    
    >>> image = load_image(choose_file())
    >>> detect_edges(image, 100)
    """
    for y in range(0, get_height(image) - 1):
        for x in range(0,get_width(image)):
            r,g,b = get_color(image, x, y)
            color = get_color(image, x, y + 1)
            top_brightness = (r + g + b)//3
            bot_brightness = (color[0] + color[1] + color[2])//3
        
            if (abs(top_brightness - bot_brightness) > threshold):
                result = create_color(0,0,0)
                set_color(image, x, y, result)
            else:
                result = create_color(255, 255, 255)
                set_color(image, x, y, result)
            
    show(image)
    return image


def detect_edges_better(image: Image,threshold: int) -> Image:
    """
    Author: Dhriti Aravind
    Return a copy of the image with the edges of the image outlined
    
    Preconditions:
    threshold value must be a real postive integer
    
    >>> image = load_image(choose_file())
    >>> detect_edges_better(image, 100)
    """   
    for y in range(0, get_height(image) - 1):
        for x in range(0,get_width(image) -1):
            r,g,b = get_color(image, x, y)
            color_down = get_color(image, x, y + 1)
            color_right = get_color(image, x + 1, y)
            top_brightness = (r + g + b)//3
            bot_brightness = (color_down[0] + color_down[1] + color_down[2])//3
            rig_brightness = (color_right[0] + color_right[1] + color_right[2])//3
        
            if (abs(top_brightness - bot_brightness) > threshold) or \
               (abs(top_brightness - rig_brightness)> threshold):
                result = create_color(0,0,0)
                set_color(image, x, y, result)
            else:
                result = create_color(255, 255, 255)
                set_color(image, x, y, result)
            
    show(image)
    return image

#copy_image = detect_edges(image, 3)

#copy_image = detect_edges_better(image, 14)


def flip_vertical(image: Image) -> Image: 
    """
    Return the image flipped vertically
    
    >>> image = load_image(choose_file())
    >>> flip_vertical(image)
    """
    centre_w = get_width(image)//2
    w = get_width(image)
    h = get_height(image)
    for x in range(centre_w -1):
        for y in range(h):
            r, g, b = get_color(image,x,y)
            r2, g2, b2 = get_color(image,abs(w-x)-1, y)
            set_color(image, x, y, create_color(r2,g2,b2))
            set_color(image, w-x-1, y, create_color(r,g,b))
            
    show(image)
    return image

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


def flip_vertical_test(vertical_image: Image, image: Image):
    """
    Author: Dhriti Aravind
    Check if the image outputted by the vertical flipper contains the
    pixel values for the original image but in "reversed" order
    
    >>> image = load_image(choose_file())
    >>> flip_vertical_test(image) 
    """
    for x in range(0, get_width(image)):
        for y in range(0, get_height(image)):
            r, g, b = get_color(image,x,y)
            r2, g2, b2 = get_color(vertical_image, x, y)
            if r == r2 and g == g2 and b == b2:
                print("TEST PASS at: "+ str(x) +" ," +str(y))
            else:
                print("TEST FAIL at: " +str(x) +" ," +str(y))
                
            
            
copy = flip_vertical(image)
flip_vertical_test(copy,image)
            
            