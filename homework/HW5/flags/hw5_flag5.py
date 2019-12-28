################################################################################
# FLAG 5
################################################################################

from turtle import *
speed(0)
def drawSquareFR (blc, w):
    """
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


#print(drawSquareFR((0,0),400))
print(drawSquareFR((0,0),250))
