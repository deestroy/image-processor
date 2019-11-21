from Cimpl import *
from L8_6_P5_vertical import *


def flip_vertical_test(vertical_image: Image, image: Image) -> None:
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
                
flip_vertical_test(copy,image)