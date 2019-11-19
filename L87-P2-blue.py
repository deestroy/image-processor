from Cimpl import *


def blue_channel(image: Image) -> Image:
    """ Author: Dhriti Aravind
    
    Return a copy of an image with only the blue component visible.
    
    >>> blue_channel(image)
    image
    
    """
    for pixel in image:
        x, y, (r, g, b) = pixel    
        blue_color = create_color(0,0,b)
        set_color(image,x,y,blue_color) 
    show(image)
    return image


def test_blue_channel(blue_image : Image):
    """ Author: Dhriti Aravind 
    
    Return whether or not the blue channel is providing only blue values in the images
    
    >>> test_blue_channel(blue_image)
    """
    for pixel in blue_image:
        x, y, (r, g, b) = pixel
        if r == 0 and g == 0:
            print("PASS : " + x + ", " + y) 
        else:
            print('FAIL @ ' + x + ", " + y) 
        
        

file = choose_file()
image = load_image(file)
blue_image = blue_channel(image)
test_blue_channel(blue_image)
