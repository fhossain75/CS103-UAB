#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# 19fa103; john k johnstone; jkj at uab dot edu; mit license

# number of words in 'le_petit_prince_utf8.txt' = ____
import random
import math
# ------------------------------------------------------------------------------
def readAndPrint (fn):
    """Read and print a text file.

    >>> readAndPrint ('short.txt')
    I am short.

    Params: fn (str) filename of the text
    Returns: (NoneType) nothing
    """
    f = open(fn, "r", encoding="utf-8")
    s=f.read()
    f.close()
    print(s)
    return

print ('#readAndPrint tests')
readAndPrint("short.txt")

# ------------------------------------------------------------------------------
def splitText (fn):
    """Split the contents of a file into tokens.

    >>> splitText ('short.txt')
    ['I', 'am', 'short.']

    Params: fn (str) filename of the text
    Returns: (str list) words in the file
    """
    f = open(fn, "r", encoding="utf-8")
    s=f.read()
    f.close()
    return s.split()

print ('#splitText tests')
print(splitText("short.txt"))
print (splitText ('le_petit_prince_utf8.txt'))
print()

# -----------------------------------------------------------------------------    
def countWord (fn):
    """Count the words in a text.

    >>> countWord ('short.txt')
    3

    Params: fn (str) filename of the text
    Returns: (int) #words
    """
    f = open(fn, "r", encoding="utf-8")
    s=f.read()
    f.close()
    ssplit = s.split()
    return len(ssplit)

print ('#countWord tests')
print(countWord("short.txt"))
print()

# ------------------------------------------------------------------------------
def lastChar (fn):
    """Build a string from the last character on each line in a text file.

    >>> lastChar ('limerick.txt')
    'nnden'
    >>> lastChar ('short.txt')
    '.'

    Notice that some lines may be empty.
    If a line is empty, the line should simply be ignored
    (since there is no last character).

    Params: fn (str) filename of the text
    Returns: (str) concatenation of the last characters on each line
    """
    f = open(fn, "r", encoding="utf-8")
    t=""
    for line in f:
        if len(line) > 1:
            t = t + line[-2]
        else:
            t=t
    f.close()
    return t

print ('#lastChar tests')
print(lastChar("limerick.txt"))
print(lastChar("canto1_commedia_dante_edited.txt"))
print()

# ------------------------------------------------------------------------------
def lastWord (fn):
    """Build a list of the last word on each line of a text.

    >>> lastWord ('limerick.txt')
    ['Lynn', 'thin', 'essayed', 'lemonade', 'in']

    Params: fn (str) filename of the text
    Returns: (str list) list of the last words on each line
    """
    f = open(fn, "r", encoding="utf-8")
    t=[]
    for line in f:
        s= line.split()
        if len(s)>1:
            t.append(s[-1])
        else:
            t=t
    f.close()
    return t

print ('#lastWord tests')
print(lastWord("limerick.txt"))
print()

# ------------------------------------------------------------------------------
def countInCircle (n):
    """Generate a random point cloud and count those inside a circle.

    - generate n random points inside [-200,200]x[-200,200].
    - write this point cloud to the file `cloud.pt`
    - count the points inside the circle of radius 200 centered at the origin
    - compute the fraction f of points that are inside the circle
    - return 4*f

    Params: n (int) size of random point cloud
    Returns: (float) 4 * fraction of the random point cloud inside the circle
    """
    f=open("cloud.pt", "a+")
    nf2 = []
    for i in range(n):
        nf2.append((random.uniform(-200,200),random.uniform(-200,200)))
    f.write(str(nf2)+"\n")
    f.close()
    f=0
    for x,y in nf2:
        if math.sqrt(abs((x-200))**2 + abs((y-200))**2) < 200:
            f+=1
        else:
            f+=0
        print(f)
    print(f)
    return 4*f

print ('#countInCircle tests')
print(countInCircle(4))
# ------------------------------------------------------------------------------    
def terzaRima (fn):
    """Test whether a text is written in terza rima.

    You may use a simplified definition of rhyming: last characters match.
    This is almost true in Italian.

    Params: fn (str) filename of the text
    Returns: (bool) is it written in terza rima?
    """
    return
# ------------------------------------------------------------------------------    
# number of words in 'le_petit_prince_utf8.txt' = ____
print("number of words in 'le_petit_prince_utf8.txt' =", countWord("le_petit_prince_utf8.txt"))
