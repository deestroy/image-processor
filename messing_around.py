from Cimpl import *


image = load_image('/Users/dhritiaravind/Documents/dog.jpg')

for pixel in image:
    x, y, (r, g, b) = pixel
    """Inverse(down)"""
    #r = 255-r
    #g = 255-g
    #b = 255-b
    #new_colour = create_color(r,g,b)
    """Gray Scale (down)"""
    #new_colour = create_color((r + g + b)//3,(r + g + b)//3 , (r + g + b)//3)
    
    """Inverse(down) """
    #if r >= 70 and r < 205:
        #new_colour = create_color(r + 50,g,b)
    #else:
        #new_colour = create_color(r - 50,g,b)
    #if g >= 70 and g < 205:
        #new_colour = create_color(r,g+50,b)
    #else:
        #new_colour = create_color(r,- 50+g,b)    
    #if b >= 70 and b < 205:
        #new_colour = create_color(r,g,b+50)
    #else:
        #new_colour = create_color(r,g,b -50) 
    
    #if r > 100: new_colour = create_color(255,g,b)
    #if g > 100:new_colour = create_color(r,255,b)
    #if b > 100:new_colour = create_color(r,g,255)
    #else: new_colour = create_color(r,g,b) 
    #set_color(image,x,y,new_colour)
    
    """EXAMPLE OF BAD CODE"""
    avg = (r+g+b)//3
    r = 255- r
    b = 255- b
    if avg>245:
        new_colour = create_color(r,g,b)
    elif avg>235:
        new_colour = create_color(g,b,r)
    elif avg>225:
        new_colour = create_color(b, r, g)
    elif avg>215:
        new_colour = create_color(r,g,b)
    elif avg>205:
        new_colour = create_color(g,b,r)
    elif avg>195:
        new_colour = create_color(b, r, g)
    elif avg>185:
        new_colour = create_color(r,g,b)
    elif avg>175:
        new_colour = create_color(g,b,r)
    elif avg>165:
        new_colour = create_color(b, r, g)
    elif avg>155:
        new_colour = create_color(r,g,b)
    elif avg>145:
        new_colour = create_color(g,b,r)
    elif avg>135:
        new_colour = create_color(b, r, g)
    elif avg>125:
        new_colour = create_color(g,b,r)
    elif avg>115:
        new_colour = create_color(b, r, g)
    elif avg>105:
        new_colour = create_color(r,g,b)
    elif avg>95:
        new_colour = create_color(g,b,r)
    elif avg>85:
        new_colour = create_color(b, r, g)
    elif avg>75:
        new_colour = create_color(r,g,b)
    elif avg>65:
        new_colour = create_color(g,b,r)
    elif avg>55:
        new_colour = create_color(b, r, g)
    elif avg>45:
        new_colour = create_color(r,g,b)
    elif avg>35:
        new_colour = create_color(g,b,r)
    elif avg>25:
        new_colour = create_color(b, r, g) 
    elif avg>15:
        new_colour = create_color(b, r, g) 
    elif avg>5:
        new_colour = create_color(b, r, g)     
    else:
        new_colour = create_color(255-r, 255-g, 255-b)
    set_color(image,x,y,new_colour)
    
    """Red"""
    #new_colour = create_color(r,0,0)
    #x = (r,0,0)
    #set_color(image,x,y,new_colour)
    
    """Green"""
    #new_colour = create_color(0,g,0)
    #y =(0,g,0)
    #set_color(image,x,y,new_colour) 
    
    """Blue"""
    #new_colour = create_color(0,0,b)
    #z = (0,0,b)
    #set_color(image,x,y,new_colour) 
    
    #c = x + y + z
    #a,d,c = c
    #new_colour = create_color(a,d,c)
    #et_color(image,x,y,new_colour) 
    
    
    

show(image)

    