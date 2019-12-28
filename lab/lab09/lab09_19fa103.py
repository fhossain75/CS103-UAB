# in-class exercises

##1. given the bottom left corner of a rectilinear square of width w, find the top right corner
# (x+y, y+w)
##2. given 2 points P and Q, find a point between them using linear interpolation,say 1/3 of the distance between P and Q
# ((1-(t)*px + (t)*qx, (1-(t))*py + (t)*qy)
##3. how could you think of the C flag in terms of lines?
# 6 Horizontal line segments
##4. how could you think of the C flag in terms of rectangles?
# 3 Filled horizontal rectangles

from turtle import *

# ------------------------------------------------------------------------------
# DO NOT CHANGE THIS FUNCTION
def drawCorners (corners):

    """Draw a set of corners in the present colour.
    Params: corners (list of int 2-tuples) corners
    """

    for i in range(len(corners)):
        up()
        goto(corners[i])
        down()
        dot(10)
# ------------------------------------------------------------------------------
# DO NOT CHANGE THIS FUNCTION (it should come in handy below)
def rectangle (blc, w, h, tk_colour):
    
    """Draw a rectilinear filled rectangle.
    Params: 
        blc (tuple): bottom left corner, the reference point
        w (int or float): width in pixels
        h (int or float): height in pixels
        tk_colour (string): Tk color specification string, for both pen and fill
    """

    up()
    goto (blc)
    down()
    setheading(0)                                              # I'm rectilinear
    color (tk_colour)                                           # make me pretty
    begin_fill()
    goto ((blc[0] + w, blc[1]))   # in the spirit of HW5, using Cartesian coords
    goto ((blc[0] + w, blc[1] + h))                # could also use forward/left
    goto ((blc[0],     blc[1] + h))
    goto (blc)
    end_fill()

# ------------------------------------------------------------------------------
def cCorners (blc, w):

    """Build a list of the corners of the C maritime flag.
    You should use linear interpolation to compute the corners.
    Remember that each corner is a point,
    so represented in Python as a tuple T of size 2 containing 2 integers,
    where T[0] is the x-coordinate and T[1] is the y-coordinate.
    Review lists and tuples if you need, since you are building 
    a list of tuples.

    Before you write the code, I would draw a picture of the flag and 
    express each of the 12 corners using linear interpolation.
    Then you can attack the Python code with a clear idea of what you are
    trying to do.
    Challenge: can you write the code using 2 for loops? That is most elegant.

    Params: 
        blc (2-tuple): bottom left corner of the C flag
        w (int): width of C flag (the square that surrounds it)
    Returns: (list of 2-tuples) corners of the C flag
    """
##    cornerlist = []
##    for x in range(12):
##        lerp
##    return

# ------------------------------------------------------------------------------
def middleRed (blc, w):
    """Draw the middle red rectangle of a maritime C flag.

    Your planning in cCorners should be useful here.

    Params: 
        blc (2-tuple): bottom left corner of the C flag
        w (int): width of C flag (the square that surrounds it)
    """
    up()
    goto (blc)
    down()
    setheading(0)                                              
    goto ((blc[0] + w, blc[1]))
    goto ((blc[0] + w, blc[1] + w))
    return

print(middleRed((0,0),10))

# ------------------------------------------------------------------------------
def cFlag (blc, w):
    """Draw a maritime C flag.

    Make sure to use other functions to help you.

    Params: 
        blc (2-tuple): bottom left corner of the C flag
        w (int): width of C flag (the square that surrounds it)
    """

    return

# ------------------------------------------------------------------------------
def randomC ():
    """Draw a maritime C flag in a random location and of a random width.
    
    Algorithm:
    - randomly generate a bottom left corner
    - randomly generate a width
    - call cFlag

    Challenge: find a random location and width that guarantees 
    the entire flag is visible.  HW5 might give you some ideas.
    """

    return

# ------------------------------------------------------------------------------
def triangle (a,b,c,tk_colour):

    """Draw a filled triangle.
    Params: 
        a,b,c (2-tuple): vertices of the triangle
        tk_colour (string): Tk color specification string, for both pen and fill
    """

    return 
# ------------------------------------------------------------------------------
# test calls follow:

# first write the cCorners function
color ('DarkViolet')
# drawCorners (cCorners ((10, 50), 100))

# another call for good measure, and to establish the code's flexibility
color ('DodgerBlue')
blc = (130, 50)
w = 125
# drawCorners (cCorners (blc, w))
# middleRed (blc, w)
# cFlag (blc, w)
# randomC ()
# triangle ((-200, 0), (0, 0), (-300,100), 'magenta')
# ------------------------------------------------------------------------------
# challenge:
def regular (n, c, L):
    
    """Draw a filled regular polygon with n sides.

    Hint 1: what is the interior angle of a regular n-gon?
    Relevant fact: the sum of the interior angles of an n-gon is 
    (n-2)*180 degrees (or (n-2)pi radians).  
    For example, 180 degrees ( pi radians) for a triangle.
                 360 degrees (2pi radians) for a square.
                 540 degrees (3pi radians) for a pentagon.
    Hint 2: use left and forward for a simpler solution

    Params: 
        n (int): # of sides of your regular polygon
        c (2-tuple): bottom left corner of polygon
        L (int): length of each edge
    """

    return
    
# color('blue')
# regular (FILL IN PARAMETERS HERE)

hideturtle() # aesthetically pleasing to remove the turtle from final drawing,
             # but you want to show the turtle and its orientation as you draw
done()       # hold on to the screen, I'm not done admiring the corners

