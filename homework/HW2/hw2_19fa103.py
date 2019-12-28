################################################################################
# HW2, CS103 Fall 2019
# name: Faisal Hossain
# blazerid: faisal75
################################################################################

################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE 'Alan Turing' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Faisal Hossain'
################################################################################

################################################################################
# helper function provided for your use in pixelLuminance: please do not change
import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
################################################################################

##############
# HW2 PROBLEMS
##############
"""
Banned: printing, strings, loops, lists, recursion
"""
# ------------------------------------------------------------------------------

def p(x):
    """Unit pluse of a value.

    >>> p(4)
    0

    Params:
    x (float) value of x
    Returns: (int) the unit pluse of x
    """
    if x<0 or x>1:
        return 0
    else:
        return 1
    
#print(p(4))
#print(p(7))
#print(p(2))
# ------------------------------------------------------------------------------

def isOdd (n):
    """ Determines whether an element is an odd integer.

    >>> isOdd(3)
    True

    Params:
    n (int) a number
    Returns (bool) a boolean value expressing whether n is an odd integer
    """
    if type(n) != int:
        return False
    elif n%2 == 0:
        return False
    else:
        return True
    
#print(isOdd(3))
#print(isOdd("n"))
#print(isOdd(3939.3))
#print(isOdd(2))
#print(isOdd(False))
#print(isOdd("1"))
# ------------------------------------------------------------------------------

def inAWhile (t, d):
    """ Time in a while on a 12 hour clock.

    >>> inAWhile(3,2)
    5

    Params:
    t (int) present time on a 12 hour clock
    d (int) increment of hour
    Returns (int) time on a 12-hour clock in d hours
    """
    assert (type(t) == int and type(d) == int)
    if t+d == 12:
        return 12
    else:
        return (t+d)%12

#print(inAWhile(12,3))
#print(inAWhile(2,3))
#print(inAWhile("t",False))
# ------------------------------------------------------------------------------

def pixelLuminance (r, g, b):
    """ Luminance of a pixel as an integer.

    >>> pixelLuminance(100,50,250)
    75

    Params:
    r (int) red intensity of a pixel (0<r<255)
    g (int) green intensity of a pixel (0<g<255)
    b (int) blue intensity of a pixel (0<b<255)
    Returns: (int) luminance of the pixel as an integer
    """
    assert (type(r) == int and type(g) == int and type(b) == int)
    assert (0<=r<=255 and 0<=g<=255 and 0<=b<=255)
    return roundHalfUp((.2126*r)+(.7152*g)+(.0722*b))

#print(pixelLuminance(100,50,250))
#print(pixelLuminance(-10,50,250))
#print(pixelLuminance(0,25,75))
# ------------------------------------------------------------------------------

def iOverlap (a1, a2, b1, b2):
    """ Determines whether two closed overlap on a real number line.

    >>> iOverlap (-54.23, -17.67, 29.46, 64.48)
    False

    Params:
    a1 (number) first closed interval of set a
    a2 (number) second closed interval of set a
    b1 (number) first closed interval of set b
    b2 (number) second closed interval of set b
    Returns: (bool) a boolean value expressing whether a and b overlap
    """
    if b1<=a1<=b2 or b1<=a2<=b2 or a1<=b1<=a2 or a1<=b2<=a2:
        return True
    elif a1>a2 or b1>b2:
        return False
    else:
        return False
    
#print(iOverlap (-40, -120, 35, 75))    
#print(iOverlap (-54.23, -17.67, 29.46, 64.48))
#print(iOverlap (-4.01, 67.55, -1.186, 5.423))
# ------------------------------------------------------------------------------

def iOverlapLen (a1, a2, b1, b2):
    """ Computes the length of overlap of two closed intervals.

    >>> iOverlapLen(-5,5,-4,4)
    8.0

    Params:
    a1 (number) first closed interval of set a
    a2 (number) second closed interval of set a
    b1 (number) first closed interval of set b
    b2 (number) second closed interval of set b
    Returns: (float) length of the overlap of closed intervals, a and b
    """
    if a1<=b1 and b2<=a2: # if b1 and b2 is between a1 and a2
        return float( (a2-a1) - ((b1-a1)+(a2-b2)) )
    elif b1<=a1 and a2<=b2: # if a1 and a2 is between b1 and b2
        return float( (b2-b1) - ((a1-b1)+(b2-a2)) )
    elif (a1>=b1 and a1<=b2) or (a1<=b2 and b2<=a2):
     # # if a1 is between b1 and b2 OR if b1 is between a1 and a2
        return float(b2-a1)
    elif (b1<=a2 and a2<=b2) or (b1>=a1 and b1<=a2):
     # if a2 is between b1 and b2 OR if b2 is between a1 and a2
        return float(a2-b1)
    else:
        return float(0)
    
#print(iOverlapLen(-5,5,-4,4))
#print(iOverlapLen(-10,-5,-8,6))
#print(iOverlapLen(-10,-7,-8,7))
#print(iOverlapLen(10,14,13,16))
# ------------------------------------------------------------------------------

def rOverlap (x1, y1, w1, h1, x2, y2, w2, h2):
    """ Determines whether two axis-aligned rectangles overlap.

    >>> rOverlap (0, 0, 5, 5, 3, 3, 3, 3)
    False

    Params:
    x1 (float) x-coordinate of the first rectangle 
    y1 (float) x-coordinate of the first rectangle 
    w1 (float) width of the first rectangle 
    h1 (float) height of the first rectangle
    x2 (float) x-coordinate of the second rectangle 
    y2 (float) x-coordinate of the second rectangle 
    w2 (float) width of the second rectangle 
    h2 (float) height of the second rectangle
    Returns: (bool) a boolean value expressing whether two rectangles overlap 
    """
    if x1<=x2<=(x1+w1) or y1<=y2<=(y1+h1):
        return True
    elif x1<=(x2+w2)<=(x1+w1):
        return True
    else:
        return False

#print(rOverlap (0, 0, 5, 5, 3, 3, 3, 3))
#print(rOverlap (0, 0, 5, 5, -3, -3, 3, 3))
#print(rOverlap (0, 0, 5, 5, -5, 5, 5, 5))
#print(rOverlap (0, 0, 5, 5, 3, 3, 4, 4))
#print(rOverlap (0, 0, 5, 5, -5, -5, -5, -5))
# ------------------------------------------------------------------------------

def rOverlapArea (x1, y1, w1, h1, x2, y2, w2, h2):
    """ Computes the area of overlap two axis-aligned rectangles.

    >>> rOverlapArea (-92.12,-59.73,78.69,86.04,-83.8,-92.42,106.0,132.2)
    False

    Params:
    x1 (float) x-coordinate of the first rectangle 
    y1 (float) x-coordinate of the first rectangle 
    w1 (float) width of the first rectangle 
    h1 (float) height of the first rectangle
    x2 (float) x-coordinate of the second rectangle 
    y2 (float) x-coordinate of the second rectangle 
    w2 (float) width of the second rectangle 
    h2 (float) height of the second rectangle
    Returns: (float) area ofoverlap of two axis-aligned rectangles
    """
    
    if x1<=x2<=(x1+w1) or y1<=y2<=(y1+h1) or x1<=(x2+w2)<=(x1+w1):
        return (x1+w1) - ((x2-x1)+((x1+w1)-(x2+w2)))
    else:
        return False
#print(rOverlapArea (0, 0, 5, 5, 3, 3, 3, 3))
#print(rOverlapArea (0, 0, 5, 5, -3, -3, 3, 3))
#print(rOverlapArea (0, 0, 5, 5, -5, 5, 5, 5))
#print(rOverlapArea (-92,-59,78,86,-83,-92,106,132))
