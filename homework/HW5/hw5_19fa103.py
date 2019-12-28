################################################################################
# HW5 CS103 Fall 2019

# I declare that I have completed this assignment completely and entirely
# on my own, without any consultation with others.
# I have read the UAB Academic Honor Code and understand that any breach
# of the Honor Code may result in severe penalties.

# name: Faisal Hossain
# blazerid: faisal75
################################################################################

from turtle import *
import random

# please add other functions to help you divide and conquer this problem
# obviously, one for each digit flag, but also functions for the components
# of a flag (the lab gave you some of the structure)
# (thought exercise: what basic units of code do you reuse several times?)
# (thought exercise: what basic units of code have a clean semantic meaning?)

################################################################################
# many other functions added here, as helper functions to natoRecur
# please include a docstring for all functions
################################################################################

#MAKE MORE HELPER FUNCTIONS, SIMPLER/CLEANER, and try making a dictionary for the drawing


"""Helper Functions"""

def blueFilledCross(w):
    
    """ Draw a filled cross square using forward and a for loop.
    Params: 
        w (int): width of each digit flag, in pixels
    """
    color("blue", "blue")
    begin_fill()
    pendown()
    forward(w/15)
    for i in range(4):
        left(-90)
        forward(w/15)
        left(90)
        forward(w/15)
        left(90)
        forward(w/15)
    end_fill()
    penup()
    
def draw0 (blc,w):
    
    """ Draw NATO flag zero.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    #black border + white background
    color("black","white")
    begin_fill()
    penup()
    goto(blc)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    end_fill()
    penup()
    #bottom left triangle
    goto(blc[0]+w/15, blc[1]+w/5)
    blueFilledCross(w)
    penup()
    #bottom right triangle
    goto(blc[0]+(w-(w/15)-(w/5)), blc[1]+w/5)
    blueFilledCross(w)
    penup()
    #upper left triangle
    goto(blc[0]+w/15, blc[1]+(w-(w/15)-(w/5)))
    blueFilledCross(w)
    penup()
    #upper right triangle
    goto(blc[0]+(w-(w/15)-(w/5)), blc[1]+(w-(w/15)-(w/5)))
    blueFilledCross(w)
    penup()
    #center triangle
    goto(blc[0]+(w/2-w/10), blc[1]+(w/2-w/30))
    blueFilledCross(w)
    penup()
    
def draw1 (blc,w):
    
    """ Draw NATO flag one.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    #rectangle 1
    color("black","red")
    begin_fill()
    pendown()
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    end_fill()
    penup()
    #rectangle 2
    color("black","yellow")
    goto(blc[0],blc[1]+w/3)
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    end_fill()
    penup()
    #rectangle 3
    color("black","red")
    goto(blc[0],blc[1]+((w/3*2)))
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    end_fill()
    penup()
    
def draw2 (blc,w):
    
    """ Draw NATO flag two.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    #rectangle 1
    color("black","yellow")
    begin_fill()
    pendown()
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    end_fill()
    penup()
    #rectangle 2
    color("black","red")
    goto(blc[0],blc[1]+w/3)
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    end_fill()
    penup()
    #rectangle 3
    color("black","yellow")
    goto(blc[0],blc[1]+((w/3*2)))
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    end_fill()
    penup()
    
def draw3 (blc,w):
    
    """ Draw NATO flag three.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    #rectangle 1
    color("black","blue")
    begin_fill()
    pendown()
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    end_fill()
    penup()
    #rectangle 2
    color("black","red")
    goto(blc[0],blc[1]+w/3)
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    end_fill()
    penup()
    #rectangle 3
    color("black","blue")
    goto(blc[0],blc[1]+((w/3*2)))
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    end_fill()
    penup()
    
def draw4 (blc,w):
    
    """ Draw NATO flag four.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    #black border + white background
    color("black","white")
    begin_fill()
    penup()
    goto(blc)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    end_fill()
    penup()
    #bottom triangle
    color("red", "red")
    begin_fill()
    penup()
    goto(blc[0]+w*.1, blc[1])
    pendown()
    goto(blc[0]+w*.9, blc[1])
    goto(blc[0]+w/2, blc[1]+w*.4)
    goto(blc[0]+w*.1, blc[1])
    end_fill()
    penup()
    #top triangle 1
    begin_fill()
    penup()
    goto(blc[0]+w*.1, blc[1]+w)
    pendown()
    goto(blc[0]+w*.9, blc[1]+w)
    goto(blc[0]+w/2, blc[1]+w*.6)
    goto(blc[0]+w*.1, blc[1]+w)
    end_fill()
    penup()
    #left triangle
    begin_fill()
    penup()
    goto(blc[0], blc[1]+w*.1)
    pendown()
    goto(blc[0], blc[1]+w*.9)
    goto(blc[0]+w*.4, blc[1]+w/2)
    goto(blc[0], blc[1]+w*.1)
    end_fill()
    penup()
    #right triangle
    begin_fill()
    penup()
    goto(blc[0]+w, blc[1]+w*.1)
    pendown()
    goto(blc[0]+w, blc[1]+w*.9)
    goto(blc[0]+w*.6, blc[1]+w/2)
    goto(blc[0]+w, blc[1]+w*.1)
    end_fill()
    penup()
    #black border
    pencolor("black")
    penup()
    goto(blc)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    penup()
def draw5 (blc,w):
    
    """ Draw NATO flag five.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    #black border + white background
    color("black","blue")
    begin_fill()
    penup()
    goto(blc)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    end_fill()
    penup()
    #bottom triangle
    color("yellow", "yellow")
    begin_fill()
    penup()
    goto(blc[0]+w*.1, blc[1])
    pendown()
    goto(blc[0]+w*.9, blc[1])
    goto(blc[0]+w/2, blc[1]+w*.4)
    goto(blc[0]+w*.1, blc[1])
    end_fill()
    penup()
    #top triangle 1
    begin_fill()
    penup()
    goto(blc[0]+w*.1, blc[1]+w)
    pendown()
    goto(blc[0]+w*.9, blc[1]+w)
    goto(blc[0]+w/2, blc[1]+w*.6)
    goto(blc[0]+w*.1, blc[1]+w)
    end_fill()
    penup()
    #left triangle
    begin_fill()
    penup()
    goto(blc[0], blc[1]+w*.1)
    pendown()
    goto(blc[0], blc[1]+w*.9)
    goto(blc[0]+w*.4, blc[1]+w/2)
    goto(blc[0], blc[1]+w*.1)
    end_fill()
    penup()
    #right triangle
    begin_fill()
    penup()
    goto(blc[0]+w, blc[1]+w*.1)
    pendown()
    goto(blc[0]+w, blc[1]+w*.9)
    goto(blc[0]+w*.6, blc[1]+w/2)
    goto(blc[0]+w, blc[1]+w*.1)
    end_fill()
    penup()
    #black border
    pencolor("black")
    penup()
    goto(blc)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    penup()
def draw6 (blc,w):
    
    """ Draw NATO flag six.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    #black border + blue background
    color("black","blue")
    begin_fill()
    penup()
    goto(blc)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    end_fill()
    penup()
    #top triangle
    color("white", "white")
    begin_fill()
    penup()
    goto(blc[0], blc[1]+w*.75)
    pendown()
    goto(blc[0]+w*.25, blc[1]+w)
    goto(blc[0], blc[1]+w)
    goto(blc[0], blc[1]+w*.75)
    end_fill()
    penup()
    #bottom triangle
    color("white", "white")
    begin_fill()
    penup()
    goto(blc[0]+w*.75, blc[1])
    pendown()
    goto(blc[0]+w, blc[1]+w*.25)
    goto(blc[0]+w, blc[1])
    goto(blc[0]+w*.75, blc[1])
    end_fill()
    penup()
    #first stripe
    color("white", "white")
    begin_fill()
    penup()
    goto(blc[0], blc[1]+w*.15)
    pendown()
    goto(blc[0], blc[1]+w*.50)
    goto(blc[0]+w*.50, blc[1]+w)
    goto(blc[0]+w*.85, blc[1]+w)
    goto(blc[0], blc[1]+w*.15)
    end_fill()
    penup()
    #second stripe
    color("white", "white")
    begin_fill()
    penup()
    goto(blc[0]+w*.15, blc[1])
    pendown()
    goto(blc[0]+w*.50, blc[1])
    goto(blc[0]+w, blc[1]+w*.50)
    goto(blc[0]+w, blc[1]+w*.85)
    goto(blc[0]+w*.15, blc[1])
    end_fill()
    penup()
    #black border
    pencolor("black")
    penup()
    goto(blc)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    penup()
    
def draw7 (blc,w):
    
    """ Draw NATO flag seven.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    #rectangle 1
    color("black","red")
    begin_fill()
    pendown()
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    end_fill()
    penup()
    #rectangle 2
    color("black","white")
    goto(blc[0]+w/3,blc[1])
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    end_fill()
    penup()
    #rectangle 3
    color("black","red")
    goto(blc[0]+((w/3*2)),blc[1])
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    end_fill()
    penup()
    
def draw8 (blc,w):
    
    """ Draw NATO flag eight.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    #rectangle 1
    color("black","yellow")
    begin_fill()
    pendown()
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    end_fill()
    penup()
    #rectangle 2
    color("black","blue")
    goto(blc[0]+w/3,blc[1])
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    end_fill()
    penup()
    #rectangle 3
    color("black","yellow")
    goto(blc[0]+((w/3*2)),blc[1])
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    end_fill()
    penup()
    
def draw9 (blc,w):
    
    """ Draw NATO flag nine.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
    """
    color("black","blue")
    begin_fill()
    pendown()
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    end_fill()
    penup()
    #rectangle 2
    color("black","white")
    goto(blc[0]+w/3,blc[1])
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    end_fill()
    penup()
    #rectangle 3
    color("black","blue")
    goto(blc[0]+((w/3*2)),blc[1])
    setheading(0)
    pendown()
    begin_fill()
    pendown()
    forward(w/3)
    left(90)
    forward(w)
    left(90)
    forward(w/3)
    left(90)
    forward(w)
    end_fill()
    penup()

def natoRecur (sn, blc, w, g):
    
    """ Using turtle graphics, draw a positive integer in NATO signal flags.

    This is the recursive function.
    In this function, the location, size, and gap are already specified.
    Digits should be drawn in the same order as the associated number.
    For example, 367 would be drawn as 3-flag gap 6-flag gap 7-flag.

    Reference: https://en.wikipedia.org/wiki/International_maritime_signal_flags

    Params: 
        sn (str) the positive integer to be drawn, as a string
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
        g (int): the gap between flags, in pixels
    """

    assert type(sn) == str
    assert type(blc) == tuple and len(blc) == 2
    assert type(w) == int and w > 0
    assert type(g) == int and g > 0
    
    drawNumbers=[]
    for i in range(len(sn)):
        drawNumbers.append("draw"+str(sn[i]))
    for i in range(len(sn)):
        penup()
        setheading(0)
        goto(blc)
        pendown()
        eval(drawNumbers[i])(blc,w)
        blc = (blc[0]+g+w,blc[1])
        
##    penup()
##    setheading(0)
##    goto(blc)
##    pendown()
##    if len(sn) == 1:
##        return sn
##    else:
##        blc = (blc[0]+g+w,blc[1])
##        return  natoRecur(sn[1:],blc,w,g)

#-------------------------------------------------------------------------------

def nato (n):

    """ Using turtle graphics, draw a positive integer in NATO signal flags.

    This function has two purposes:
    1) to randomize the position/size/gap of the flag
    2) to cast the number to a string, for simpler recursion

    Algorithm:
    - randomize the location of the first flag:
      the Cartesian coordinates blc = (px,py) of the bottom left corner 
      of the first digit should to be chosen at random
      within the square bounded by (-400,-100) and (-350,0)

    - randomize the size of the flags:
      the width w of each digit should be chosen at random 
      so that 50 <= w <= 100 (use the same width for all digits)

    - randomize the gap between consecutive flags:
      the gap g between consecutive digits should be chosen at random
      so that 1 <= g <= 10

    - cast n to a string 
    - call natoRecur, the recursive function that does the rest of the work

    Params: 
        n (int) the positive integer to be drawn (n>0)
    """
    sn = str(n)
    blc = (random.randint(-400,-100), random.randint(-350,0))
    w = random.randint(50,100)
    g = random.randint(1,10)
    print(blc,w,g)
    return natoRecur (sn, blc, w, g)

#print(nato(9528704316))
################################################################################
speed(0)                             # draw at max speed, to help the TA's grade
             # while you are debugging, I suggest slowing this to, say, speed(3)
n = random.randint (100,99999999999) 
print ('my random number to draw is ' + str(n))
# while debugging, you should set n to something simpler, e.g., n = 12
# as you get close, then test with the present version
# and when you submit, leave it this way (using random n)
# n = 12 # example of test data as you develop (overriding the n above)
nato (n)
hideturtle()                                              # make me pretty
done()                                                    # keep the window open

# Since we will not use an autograder for this homework,
# please leave this test call in your code.
# This will allow TA's to run your code easily.
# It will also allow you to test your code
