from Cimpl import *

file = choose_file()
image = load_image(file)


def three_tone(image: Image, color1: str, color2: str, color3: str) -> Image:
    """ Author: Dhriti Aravind
    Return an image with only three tones with specified colours from the user.
   
    >>> image = load_image(choose_file())
    >>> three_tone_image = three_tone(image, "yellow", "green", "blue")
    >>> show(three_tone_image)
    """     
    
    for pixel in image:
        x, y, (r, g, b) = pixel
        avg_color = (r+g+b)/3
        colors = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
        color_values = [(0,0,0), (255,255,255),(255,0,0),(0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255),(128,128,128) ]
        
        for i in range(len(colors)):
            if color1 == colors[i]:
                c1 = color_values[i]
                
        for i in range(len(colors)):
            if color2 == colors[i]:
                c2 = color_values[i]
        
        for i in range(len(colors)):
            if color3 == colors[i]:
                c3 = color_values[i]
                
        if avg_color >= 0 and avg_color <= 84:
            result = create_color(c1[0],c1[1],c1[2])
        elif avg_color >= 85 and avg_color <= 170:
            result = create_color(c2[0],c2[1],c2[2])
        elif avg_color >= 171 and avg_color <= 255:
            result = create_color(c3[0],c3[1],c3[2])  
            
        set_color(image, x, y, result)
    show(image)
    return image    
copy_image2 = three_tone(image, "black", "cyan", "white")