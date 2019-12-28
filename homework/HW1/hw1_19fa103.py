################################################################################
# HW1, CS103 Fall 2019
# name: Faisal Hossain (but also insert your name in the function myName below)
# blazerid: faisal75
################################################################################

import math      # you will need the math module to answer some of the questions

################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE 'Alan Turing' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Faisal Hossain'
################################################################################

##############
# HW1 PROBLEMS
##############		

def f(x):                   # this is a practice problem that will not be graded
    return 5*x-3

def areaCircle (r):
    return math.pi*r**2

def nSnookerBall (nRow):
    return int((nRow*(nRow+1))/2)

def eApproximately (n): 
    return (1+(1/n))**n

def volCone (r, h):
    return (1/3)*math.pi*(r**2)*h

def distOrigin (x, y):
    return math.sqrt((x**2)+(y**2)) 

def lengthSegment (x1, y1, z1, x2, y2, z2):
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2))
