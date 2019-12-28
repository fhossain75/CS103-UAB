# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# lab012 on Mondrian

from turtle import *
import random
import math
speed(0)
# ------------------------------------------------------------------------------

def border(blc,w):
    """Draws a black border for the work of art.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost work of art
        w (int): width of the work of art
    """
    pencolor("black")
    penup()
    goto(blc)
    pendown()
    for i in range(4):
        forward(w)
        left(90)
    penup()

def vertLines(blc, w, n, randVert):
    """Draws a defined number of vertical lines within the borders.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost work of art
        w (int): width of the work of art
        n (int): number of lines and filled squares
        randVert (list): list of x-coordinates of the vertical lines
    """
    for i in range(n):
        x = random.randint(blc[0],blc[0]+w)
        goto(x,blc[1])
        setheading(90)
        pendown()
        forward(w)
        penup()
        randVert.append(x)
        
def horzLines(blc, w, n, randHorz):
    """Draws a defined number of horizontal lines within the borders.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost work of art
        w (int): width of the work of art
        n (int): number of lines and filled squares
        randHorz (list): list of y-coordinates of the horizontal lines
    """
    for i in range(n):
        y = random.randint(blc[1],blc[1]+w)
        goto(blc[0],y)
        setheading(0)
        pendown()
        forward(w)
        penup()
        randHorz.append(y)

def filledSquares(n, randVert, randHorz):
    """Draws a defined number of filled squares within the intersecting lines.
    Params:
        n (int): number of lines and filled squares
        randVert (list): list of x-coordinates of the vertical lines
        randHorz (list): list of y-coordinates of the horizontal lines
    """
    colors = ["red","blue","black","violet","grey","gold","green"]
    for i in range(n):
        rx = random.randint(0,n-2)
        ry = random.randint(0,n-2)
        fillcolor(random.choice(colors))
        begin_fill()
        goto(randVert[rx], randHorz[ry])
        goto(randVert[rx], randHorz[ry+1])
        goto(randVert[rx+1], randHorz[ry+1])
        goto(randVert[rx+1], randHorz[ry])
        goto(randVert[rx], randHorz[ry])
        end_fill()
    penup()

def Mondrian(blc, w, n):
    
    """Draw a work of art in the style of (inspired by) Mondrian.
    Params:
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost work of art
        w (int): width of the work of art
        n (int): number of lines and filled squares
    """
    randVert = []
    randHorz = []
    pensize(random.randint(0,10))
    border(blc,w)
    pencolor("black")
    vertLines(blc, w, n, randVert)
    horzLines(blc, w, n, randHorz)
    filledSquares(n, randVert, randHorz)


print(Mondrian((-200,-100), 400, 5))

#still need to find a way where restrict the same boxes from being filled again
#...  but I have a final tomorrow
