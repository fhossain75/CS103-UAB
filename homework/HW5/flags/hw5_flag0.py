################################################################################
# FLAG 0
################################################################################

from turtle import *
speed(0)

def blueFilledCross(w):
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
    
def drawSquareFR (blc, w):
    """
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
#print(drawSquareFR((0,0),400))
print(drawSquareFR((0,0),200))
