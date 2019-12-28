# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# render the lab07 exercises
#
# you don't have to read this code, just run the script:
# python lab07_render_19fa103.py (use tab completion to speed this typing up)
# 
# read code if you please, for fun: no worries if you don't fully understand it
# and no worries if you decide to skip reading it

from lab07_19fa103 import *
from turtle import *

def drawPolygon (L):

    """Draw a polygon.
    Params: L (list of 2-tuples): the vertices of a polygon
    """

    up()
    goto (L[0])
    down()
    for i in range(1,len(L)):
        goto (L[i])
    goto (L[0])

def drawCloud (pt, c, scale=1):

    """Draw a point cloud.

    Params: 
        pt (list of 2-tuples): point cloud in 2-space
        c (string): colour of each point
    """

    for p in pt:
        up ()
        goto (p[0]*scale, p[1]*scale)
        down ()
        dot (3, c)


# speed(0)
hideturtle()
print ('drawing a triangle (once you have completed the code) ...')
p = randTri2 (100)
if p != None:
    drawPolygon (p)             # in spirit of generalization, draw as a polygon
foo = input ('Enter return whenever you are ready.')
clear()

print ('drawing a point cloud, version 1 of uniform distribution...')
p = randCld2_v1(200., 100)
if p != None:
    tracer(0,0)                                        # turn screen updates off
    drawCloud (p, 'blue')
    update()                                           # update the screen again
foo = input ('Enter return whenever you are ready.')
clear()

print ('drawing a point cloud, version 2 of uniform distribution...')
p = randCld2_v2(200., 100)
if p != None:
    tracer(0,0)
    drawCloud (p, 'red')
    update()
foo = input ('Enter return whenever you are ready.')
clear()

print ('drawing a point cloud, Gaussian distribution...')
tracer(0,0)
if p != None:
    p = randGaussCld2 (50, 100)
    drawCloud (randGaussCld2 (50, 100), 'magenta')
    update()
foo = input ('Enter return whenever you are ready.')
clear()

print ('drawing a random set of unit vectors, uniformly sampled')
print ('we are scaling up by a factor of 200, so that you can see them')
p = randCldUnit2 (20)
if p != None:
    tracer(0,0)
    drawCloud (p, 'black', 200)
    update()
foo = input ('Enter return whenever you are ready.')
