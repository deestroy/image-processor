from Cimpl import *
from L87-P2-channel-filters import *

file = choose_file()
image = load_image(file)  

def combine(red_image: Image, green_image: Image, blue_image: Image, image: Image):
    """Author: Dhriti Aravind
    
    Displays a combined image using the values of the red, green and blue images
    
    >>> combine(red_image, green_image, blue_image, image)
    image
    """
    for pixel in image:
        red = get_color(red_image, x, y)
        r = red[0]
        green = get_color(green_image,x,y)
        g = green[1]
        blue = get_color(blue_image, x, y)
        b = blue[2]
        comb = (image, r, g, b)
        set_color(image, x, y, comb)
    show(image)
    return image

def test_combine(red_image: Image, green_image: Image, blue_image: Image, combined_image: Image) -> Image:
    """Author: Dhriti Aravind
    
    Tests to check if the red, green and blue values in the combined image match 
    those of the red, green and blue image.
    
    >>> test_combine(red_image, green_image, blue_image, combined_image)
    
    """
    for x, y, (r,g,b) in combined_image:
        red = get_color(red_channel,x,y)
        green = get_color(green_channel,x,y)
        blue = get_color(blue_channel,x,y)
        
        if r == red[0] and g == green[1] and b == blue[2]:
            print("PASS at coordinate: " + x + "," + y)
            pass
        else:
            print("FAIL at coordinate: " + x + ", " + y + " producing " + r + "," + g + "," + b)
            

blue_image = blue_channel(image)
green_image = green_channel(image)
red_image = red_channel(image)
combined_image = combine(red_image,green_image,blue_image, image)
test_combine(red_image, green_image, blue_image, combined_image)
    