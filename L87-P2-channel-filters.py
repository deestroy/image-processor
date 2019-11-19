from Cimpl import *

file = choose_file()
image = load_image(file)            


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

def green_channel(image: Image)-> Image: #Jack Rowlatt
    """returns a copy of the old image, with only the green components visible.
    """
    for pixel in image:
        x, y, (r,g,b) = pixel
        green = create_color(0,g,0)
        set_color(image, x, y, green)
    show(image) 
    return image

def red_channel(image: Image)-> Image: #Jack Rowlatt
    """returns a copy of the old image, with only the red components visible.
    """
    for pixel in image:
        x, y, (r,g,b) = pixel
        red = create_color(r, 0, 0)
        set_color(image, x, y, red)
    show(image)
    return image 
    
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

def test_blue_channel(blue_image: Image):
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

def test_red_channel(red_image: Image):
    """ Author: Dhriti Aravind 
    
    Return whether or not the red channel is providing only red values in the images
    
    >>> test_red_channel(red_image)
    """
    for pixel in red_image:
        x, y, (r, g, b) = pixel
        if g == 0 and b == 0:
            print("PASS : " + x + ", " + y) 
        else:
            print('FAIL @ ' + x + ", " + y) 

def test_green_channel(green_image: Image):
    """ Author: Dhriti Aravind 
    
    Return whether or not the green channel is providing only green values in the images
    
    >>> test_green_channel(green_image)
    """
    for pixel in green_image:
        x, y, (r, g, b) = pixel
        if r == 0 and b == 0:
            print("PASS : " + x + ", " + y) 
        else:
            print('FAIL @ ' + x + ", " + y) 
            
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
test_blue_channel(blue_image)
green_image = green_channel(image)
test_green_channel(green_image)
red_image = red_channel(image)
test_red_channel(red_image)
combined_image = combine(red_image,green_image,blue_image, image)
test_combine(red_image, green_image, blue_image, combined_image)
    