################################################################################
# FLAG 3
################################################################################

from turtle import *
speed(0)
def drawSquareFR (blc, w):
    """
    """
    #black border
##    pencolor("black")
##    penup()
##    goto(blc)
##    pendown()
##    for i in range(4):
##        forward(w)
##        left(90)
##    penup()
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
    
print(drawSquareFR((0,0),250))
