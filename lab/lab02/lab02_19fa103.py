# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# ------------------------------------------------------------------------------
def firstLetter (s):                        
    """First letter of a string (a version similar to HW1 submission style).
    >>> firstLetter ('garden')
    g
    Params: s (string) a string of length at least 1
    Returns: (string) first letter of s
    """
    return s[0]

print ('firstLetter test calls')
print (firstLetter ('garden'))                # expected output 'g'
print (firstLetter ('abracadabra'))           # expected output 'a'
print (firstLetter ('this is also a string')) # expected output 't'
# try calling firstLetter(1) and firstLetter(''): what happens?
# print (firstLetter(1))
# ------------------------------------------------------------------------------
def firstLetterNice (s):                      
    """First letter of a string (a version with assertions added).
    >>> firstLetterNice ('garden')
    g
    Params: s (string) a string of length at least 1
    Returns: (string) first letter of s
    """
    assert (type(s) == str)         # one assertion at a time
    assert (len(s) > 0)
    return s[0]

print ()
print ('firstLetterNice test calls')
print (firstLetterNice ('garden'))
# try calling firstLetterNice(1) and firstLetterNice (''): what happens?
# print (firstLetterNice(1))
# ------------------------------------------------------------------------------
def secondLetter (s):

    """Second letter of a string (HW1 submission version).
    >>> secondLetter ('garden')
    a
    Params: s (string) a string of length at least 2
    Returns: (string) second letter of s
    """
    return s[1]

print ()
print ('secondLetter test calls')
print (secondLetter ('garden'))
# add your own test data
# ------------------------------------------------------------------------------
def secondLetterNice (s):

    """Second letter of a string (assertion version).
    >>> secondLetterNice ('garden')
    a
    Params: s (string) a string of length at least 2
    Returns: (string) second letter of s
    """
    assert (type(s) == str)                            
    assert (len(s) >= 2)
    return s[1]

print ()
print ('secondLetterNice test calls')
print (secondLetterNice ('garden'))
# add your own test data
print (secondLetterNice ('Johnstone'))
#print (secondLetterNice ('F'))   # example of assert statement deployed
# ------------------------------------------------------------------------------
def lastLetter (s):

    """Last letter of a nonempty string (HW1 submission version).
    >>> lastLetter ('garden')
    n
    Params: s (string) a nonempty string
    Returns: (string) last letter of s
    """
    return s[-1]

print ()
print ('lastLetter test calls')
print (lastLetter ('garden'))
# add your own test data
print (lastLetter ('Johnstone'))
# ------------------------------------------------------------------------------
def lastLetterNice (s):

    """Last letter of a nonempty string (assertion version).
    >>> lastLetterNice ('garden')
    n
    Params: s (string) a nonempty string
    Returns: (string) last letter of s
    """
    assert (type(s) == str)                            
    assert (len(s) > 0)
    return s[-1]

print ()
print ('lastLetterNice test calls')
print (lastLetterNice ('garden'))
#print (lastLetterNice (10))   # example of assert statement deployed
#print (lastLetterNice (""))   # example of assert statement deployed
# ------------------------------------------------------------------------------
import string
def isPunctNice (s):
    
    """Determine if a character is punctuation (assertion version).
    >>> isPunctNice ('g')
    False

    Params: s (string) a single character (len(s) == 1)
    Returns: (bool) is this a punctuation character?
    """
    assert (len(s) == 1)
    return s in string.punctuation

print ()
print ('isPunctNice test calls')
print (isPunctNice ('a')) 
print (isPunctNice ('.')) 
#print (isPunctNice ('!!'))   # example of assert statement deployed
# ------------------------------------------------------------------------------
# Euclidean distance functions

import math
def length2 (x,y):
    """Euclidean length of a vector in 2-space.
    >>> length2(1,-1)
    1.4142135623730951
    Params:
        x (float): x-coordinate of a vector v in 2-space
        y (float): y-coordinate of a vector v in 2-space
    Returns: Euclidean norm of the vector v
    """
    return math.sqrt((x**2)+(y**2))

# add at least one function call on test data
print ()
print ('length2 test calls')
print(length2(1,-1))
print(length2(3,9))
# ------------------------------------------------------------------------------
def length3 (x,y,z):
    """Euclidean length of a vector in 3-space.
    >>> length2(1,-1,2)
    2.449489742783178
    Params:
        x (float): x-coordinate of a vector v in 3-space
        y (float): y-coordinate of a vector v in 3-space
        z (float): z-coordinate of a vector v in 3-space        
    Returns: Euclidean norm of the vector v
    """
    return math.sqrt((x**2)+(y**2)+(z**2))

# add at least one function call on test data
print ()
print ('length3 test calls')
print(length3(1,-1,2))
print(length3(3,9,4))
# ------------------------------------------------------------------------------
def dist2 (x1,y1,x2,y2):
    """Euclidean distance between two points in 2-space.
    >>> dist2(1,1,2,2)
    1.4142135623730951
    Params:
        x1 (float): x-coordinate of a point p in 2-space
        y1 (float): y-coordinate of p
        x2 (float): x-coordinate of a point q in 2-space, q != p
        y2 (float): y-coordinate of q
    Returns: Euclidean distance between p and q
    """
    q = (x1,y1)
    p = (x2,y2)
    assert (q != p)
    return math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )

# add at least one function call on test data
print ()
print ('dist2 test calls')
print(dist2(1,1,2,2))
print(dist2(1,2,2,1))
#print(dist2(2,1,2,1))     # example of assert statement deployed
# ------------------------------------------------------------------------------
def dist3 (x1,y1,z1,x2,y2,z2):
    """Euclidean distance between two points in 3-space.
    >>> dist3(1,1,2,2,3,3)
    2.449489742783178
    Params:
        x1 (float): x-coordinate of a point p in 3-space
        y1 (float): y-coordinate of p
        z1 (float): z-coordinate of p
        x2 (float): x-coordinate of a point q in 3-space, q != p
        y2 (float): y-coordinate of q
        z2 (float): z-coordinate of q
    Returns: Euclidean distance between p and q
    """
    q = (x1,y1,z1)
    p = (x2,y2,z2)
    assert (q != p)
    return math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2) )

# add at least one function call on test data
print ()
print ('dist3 test calls')
print(dist3(1,1,2,2,3,3))
print(dist3(1,1,1,2,2,2))
print(dist3(5,7,9,9,7,5))
#print(dist3(9,7,5,9,7,5))   # example of assert statement deployed
# ------------------------------------------------------------------------------
'''The 4 formulae for Euclidean distance
length2 (x,y) - the square root of the sum of x-coordinate squared and y-coordinate squared
length3 (x,y) - the square root of the sum of x-coordinate squared, y-coordinate squared, and z-coordinate squared
dist2 (x1, y1, x2, y2) - the square root of the sum of the squared difference of x-coordinate of a point p minus x-coordinate of a point q and the squared difference of y-coordinate of a point p minus y-coordinate of a point q
dist3 (x1, y1, z1, x2, y2, z2) - the square root of the sum of the squared difference of x-coordinate of a point p minus x-coordinate of a point q, the squared difference of y-coordinate of a point p minus y-coordinate of a point q, the squared difference of z-coordinate of a point p minus z-coordinate of a point q

[Challenge] Proof of the 3-space case √(x2+ y2 + z2)
– (x,y,z) is a vector in 3-space
– project it to (x,y,0) and consider the right triangle formed
– length of one side is √(x2+ y2) by the 2-space formula
– length of other side is z
– squared length of hypotenuse is (√(x2+ y2))2+ z2= x2+ y2+ z2
Given in 9/10 lecture.
'''
