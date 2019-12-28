# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# lab06: turtle graphics

from turtle import *

# ------------------------------------------------------------------------------
def drawLine1 (a, heading, length):

    """Draw a line segment using forward. (Note how awkward the parameters are.)

    >>> drawLine1 ((0,0), 45, 100)

    Params: 
        a (2-tuple): an endpoint of the line segment
        heading (int): angle in degrees of the line segment, from +ve x-axis
        length (int): length of the line segment 
                      (the 2nd endpt lies at given heading this distance from a)
    """
    pencolor("red")
    penup()
    goto(a)
    setheading(heading)
    pendown()
    forward(length)
    return

#drawLine1 ((0,0), 45, 100)
#drawLine1 ((-10,30),-45, 100)
# ------------------------------------------------------------------------------
def drawLine2 (a,b):

    """Draw a line segment using goto.  Ah, nice.

    >>> drawLine2 ((0,0), (100,100))  
    (no, this is not the same line as the test data for drawLine1: why?)

    Params: 
        a (2-tuple): an endpoint of the line segment
        b (2-tuple): the other endpoint of the line segment
    """
    pencolor("orange")
    penup()
    goto(a)
    pendown()
    goto(b)
    penup()
    
#drawLine2((0,0),(0,-100))
# ------------------------------------------------------------------------------
def drawSquareFL (c, w):

    """Draw a rectilinear square using forward, left, and a for loop.

    >>> drawSquareFL ((0,0), 100)

    Params:
        c (2-tuple): bottom left corner of the square
        w (int):     width of the square, in pixels
    Returns: None
    """
    pencolor("aqua")
    penup()
    setheading(0)
    goto(c)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    penup()
    
#drawSquareFL((0,0),100)
# ------------------------------------------------------------------------------
def drawSquareG (c, w):

    """Draw a rectilinear square using goto (no forward).
    No need for a for loop this time.

    >>> drawSquareG ((0,0), 100)

    Hint: this is the preferred way for HW4.
    Hint: tuples use indexing just like strings and lists.
    Hint: what are the Cartesian coordinates of the 4 corners?

    Params:
        c (2-tuple): bottom left corner of the square
        w (int):     width of the square
    """
    pencolor("green")
    penup()
    goto(c)
    pendown()
    goto(c[0]+w,c[1])
    goto(c[0]+w,c[1]+w)
    goto(c[0],c[1]+w)
    goto(c[0],c[1])
    penup()

#drawSquareG ((0,100), 100)
# ------------------------------------------------------------------------------
def drawSquareFR (c, w):

    """Draw a filled rectilinear square using forward, right, and a for loop.

    >>> drawSquareFR ((0,0), 100)

    Hint: start by cut and paste of the code from drawSquareFL, then tweak.

    Params:
        c (2-tuple): bottom left corner of the square
        w (int):     width of the square
    """
    color("blue","blue")
    penup()
    goto(c)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    penup()
    
#drawSquareFR((-100,0),100)
# ------------------------------------------------------------------------------
def drawSquare (c, a, w):

    """Draw a non-rectilinear square (forward is much easier than goto here).

    >>> drawSquare ((0,0), 10, 100)

    Hint: small tweak of drawSquareFL

    Params:
        c (2-tuple): bottom left corner of the square
        a (int):     angle of square from +ve x-axis in degrees 
                     (initial heading)
        w (int):     width of square
    """
    pencolor("purple")
    penup()
    setheading(a)
    goto(c)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    penup()
    
#drawSquare((100,200),10,100)
# ------------------------------------------------------------------------------
def drawTriFL (c, a, L):

    """Draw an equilateral triangle using forward, left, and a for loop.

    >>> drawTriFL ((0,0), 10, 100)

    Params:
        c (2-tuple): bottom left corner of the triangle
        a (int):     angle of first side from +ve x-axis in degrees 
                     (initial heading)
        L (int): length of a side
    """
    pencolor("maroon")
    penup()
    goto(c)
    pendown()
    setheading(a)
    for i in range(3):
        forward(L)
        left(120)
    penup()
    
#drawTriFL ((-100,100), 10, 100)
# ------------------------------------------------------------------------------
def drawTri (p, q, r):

    """Draw a triangle using goto.  This is the preferred way.
    No for loop here. (How would you change the parameters to allow a for loop?)

    >>> drawTri ((0,0), (100,0), (50, 50))

    Params:
        p (2-tuple): 1st vertex
        q (2-tuple): 2nd vertex
        r (2-tuple): 3rd vertex
    """
    pencolor("navy blue")
    penup()
    goto(p)
    pendown()
    goto(q)
    pendown()
    goto(r)
    goto(p)
    penup()

#drawTri ((0,0), (100,0), (50, 50))
#drawTri ((-50,-50), (-100,0), (0, 0))
# ------------------------------------------------------------------------------
def drawFilledTri (c, a, L):

    """Draw a filled equilateral triangle using forward, right, and a for loop.

    >>> drawFilledTri ((0,0), 120, 100)

    Hint: the code for drawTriFL may be a good starting point for this code

    Params:
        c (2-tuple): bottom left corner of the triangle
        a (int):     angle of first side from +ve x-axis in degrees 
                     (initial heading)
        L (int): length of a side
    """
    color("gold", "gold")
    begin_fill()
    penup()
    goto(c)
    pendown()
    setheading(a)
    for i in range(3):
        forward(L)
        left(120)
    end_fill()
    penup()

#drawFilledTri ((-100,0), 120, 100)
#drawFilledTri ((100,-100), 100, 10)
