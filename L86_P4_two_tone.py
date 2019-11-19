from Cimpl import *

file = choose_file()
image = load_image(file)

def two_tone(image: Image, color1: str, color2: str) -> Image:
    """ Author: Dhriti Aravind
    Return an image with only two tones with specified colours from the user.
   
    >>> image = load_image(choose_file())
    >>> two_tone_image = two_tone(image, "yellow", "green")
    >>> show(two_tone_image)
    """    
    for pixel in image:
        x, y, (r, g, b) = pixel
        avg_color = (r+g+b)/3
        
        #DEFINES the colors and the number values associated (1st value in colors corresponds to the 1st color tuple of the color_values)
        colors = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
        color_values = [(0,0,0), (255,255,255),(255,0,0),(0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255),(128,128,128)]
        
        #Uses the color inputted by the user and determines the number values
        for i in range(len(colors)):
            if color1 == colors[i]:
                c1 = color_values[i]
                
        for i in range(len(colors)):
            if color2 == colors[i]:
                c2 = color_values[i]
        
        
        if avg_color >= 0 and avg_color <= 127:
            result = create_color(c1[0],c1[1],c1[2])
            set_color(image, x, y, result)
        elif avg_color >= 128 and avg_color <=255:
            result = create_color(c2[0],c2[1],c2[2])
        set_color(image, x, y, result)     
        
    show(image)
    return image    

copy_image = two_tone(image, "red", "cyan")
#copy_image2 = three_tone(image, "black", "cyan", "white")


