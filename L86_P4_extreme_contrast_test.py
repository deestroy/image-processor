from Cimpl import *
filename = choose_file()
image = load_image(filename)
contrast_image = copy(image)

def extreme_contrast(image) -> image:
    """ Author: Jack Rowlatt"""
    
    for pixel in image:
        x, y, (r,g,b) = pixel
        image_color= get_color(image, x, y)
        if image_color[0] <= 127:
            r = 0
        elif image_color[0] > 127:
            r = 255
        if image_color[1] <= 127:
            g = 0
        elif image_color[1] > 127:
            g = 255
        if image_color[2] <= 127:
            b = 0
        elif image_color[2] > 127:
            b = 255
        contrast = create_color(r, g, b)
        set_color(contrast_image, x, y, contrast)
    show(contrast_image)
    return contrast_image
extreme_image = extreme_contrast(contrast_image)

def extreme_constrast_test(extreme_image: Image):
    """ Author: Dhriti Aravind
    
    Test each pixel to ensure that the picture for the extreme_contrast gives the rgb
    gives a 0 value or a 255 value for each component
    
    >>> extreme_constrast_test(extreme_image)

    """
    for pixel in extreme_image:
        x,y,(r,g,b) = pixel
        if (r == 255 or r == 0) and (g == 255 or g==0) and (b == 255 or b == 0):
            print("PASS at : "+ str(x) +", " + str(y))
    
        else:
            print("FAIL at : "+ str(x) +", " + str(y))

extreme_constrast_test(extreme_image)
            