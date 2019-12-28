################################################################################
# FLAG 6
###############################################################################

from turtle import *
speed(0)
def drawSquareFR (blc, w):
    """
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
    goto(blc[0], blc[1]+w*.25)
    pendown()
    goto(blc[0], blc[1]+w*.50)
    goto(blc[0]+w*.50, blc[1]+w)
    goto(blc[0]+w*.75, blc[1]+w)
    goto(blc[0], blc[1]+w*.25)
    end_fill()
    penup()
    #second stripe
    color("white", "white")
    begin_fill()
    penup()
    goto(blc[0]+w*.25, blc[1])
    pendown()
    goto(blc[0]+w*.50, blc[1])
    goto(blc[0]+w, blc[1]+w*.50)
    goto(blc[0]+w, blc[1]+w*.75)
    goto(blc[0]+w*.25, blc[1])
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

#print(drawSquareFR((0,0),400))
print(drawSquareFR((0,0),200))
