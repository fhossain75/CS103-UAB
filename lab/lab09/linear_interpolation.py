# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# hint: linear interpolation should help you design your flag in HW2

from turtle import *

def lerp (P, Q, t):

    """Linear interpolation between P and Q.
    
    >>> lerp ((0, 0), (10, 0), .2)
    (2, 0)
    >>> lerp ((1, 2), (9, 10), .5)
    (5, 6)
    
    Params: 
        P (2-tuple): Cartesian coordinates of a point in 2-space
        Q (2-tuple): Cartesian coordinates of another point in 2-space
        t (float)  : parameter of linear interpolation
    Returns: (2-tuple) (1-t)P + tQ, a point 
    """

    return ((1-t)*P[0] + t*Q[0],
            (1-t)*P[1] + t*Q[1])


def turtlyLineSegment (P, Q):
            
    """Use linear interpolation to move the turtle along the line segment PQ.
    Params: 
        P (2-tuple): Cartesian coordinates of a point in 2-space
        Q (2-tuple): Cartesian coordinates of another point in 2-space
    """

    up()
    goto (P)
    down()
    delta = .01                         # can be adjusted; could be a parameter!
    t = delta
    while t < 1:
        goto (lerp(P,Q,t))
        t = t + delta
    goto (Q)                                               # get there perfectly

color ('DarkViolet')                                       # I want to be pretty
hideturtle()                                               # and discrete
turtlyLineSegment ((-200,-200), (200,200))
done()
