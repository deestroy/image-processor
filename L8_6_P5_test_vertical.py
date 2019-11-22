from Cimpl import *
from L8_6_P5_vertical import *


#def flip_vertical_test(vertical_image: Image, image: Image) -> None:
    #"""
    #Author: Dhriti Aravind
    #Check if the image outputted by the vertical flipper contains the
    #pixel values for the original image but in "reversed" order
    
    #>>> image = load_image(choose_file())
    #>>> flip_vertical_test(image) 
    #"""
    #for x in range(0, get_width(image)):
        #for y in range(0, get_height(image)):
            #r, g, b = get_color(image,x,y)
            #r2, g2, b2 = get_color(vertical_image, x, y)
            #if r == r2 and g == g2 and b == b2:
                #print("TEST PASS at: "+ str(x) +" ," +str(y))
            #else:
                #print("TEST FAIL at: " +str(x) +" ," +str(y))
                
#flip_vertical_test(copy,image)

def check_equal(description: str, outcome, expected) -> None:
    """
    Author: Donald Bailey
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        # The format method is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")
    
def flip_vertical_test() -> None:
    """
    Print "PASSED" message in the shell if the outcome is the same as expected,
    otherwise, print "FAILED" along with the associated coordinates.
    """
    
    #Create an image with 15 pixels
    original = create_image(5, 3)
    set_color(original, 0, 0,  create_color(1, 1, 15))
    set_color(original, 1, 0,  create_color(1, 2, 14))
    set_color(original, 2, 0,  create_color(1, 3, 13))
    set_color(original, 3, 0,  create_color(1, 4, 12))
    set_color(original, 4, 0,  create_color(1, 5, 11))
    
    set_color(original, 0, 1,  create_color(1, 6, 10))
    set_color(original, 1, 1,  create_color(1, 7, 9))
    set_color(original, 2, 1,  create_color(1, 8, 8))
    set_color(original, 3, 1,  create_color(1, 9, 7))
    set_color(original, 4, 1,  create_color(1, 10, 6))
    set_color(original, 0, 2,  create_color(1, 11, 5))
    set_color(original, 1, 2,  create_color(1, 12, 4))
    set_color(original, 2, 2,  create_color(1, 13, 3))
    set_color(original, 3, 2,  create_color(1, 14, 2))
    set_color(original, 4, 2,  create_color(1, 15, 1))
    
    #Create the expected outcome for the original image
    #Should provide the outcome after the original is passed in.
    
    expected = create_image(5, 3)
    set_color(expected, 0, 0,  create_color(1, 5, 11))
    set_color(expected, 1, 0,  create_color(1, 4, 12))
    set_color(expected, 2, 0,  create_color(1, 3, 13))
    set_color(expected, 3, 0,  create_color(1, 2, 14))
    set_color(expected, 4, 0,  create_color(1, 1, 15))
    
    set_color(expected, 4, 1,  create_color(1, 6, 10))
    set_color(expected, 3, 1,  create_color(1, 7, 9))
    set_color(expected, 2, 1,  create_color(1, 8, 8))
    set_color(expected, 1, 1,  create_color(1, 9, 7))
    set_color(expected, 0, 1,  create_color(1, 10, 6))
    
    set_color(expected, 4, 2,  create_color(1, 11, 5))
    set_color(expected, 3, 2,  create_color(1, 12, 4))
    set_color(expected, 2, 2,  create_color(1, 13, 3))
    set_color(expected, 1, 2,  create_color(1, 14, 2))
    set_color(expected, 0, 2,  create_color(1, 15, 1))
   
    #Compare image outputted by function to the expected image of flip_vertical.
    #Check each pixel
    vertical_image = flip_vertical(original)
    for x, y, col, in vertical_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

flip_vertical_test()