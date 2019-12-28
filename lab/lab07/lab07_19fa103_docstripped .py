# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# lab07 on randomization

import random
import math

# skipping test calls in the docstrings, since they are random

# ------------------------------------------------------------------------------
def randPt2 (r):

    x = round(random.uniform(-r,r),2)
    y = round(random.uniform(-r,r),2)
    return (x,y)

print("#randPt2 Test")
print (randPt2(10))
print()
# ------------------------------------------------------------------------------
def randPt3 (r):

    x = round(random.uniform(-r,r),2)
    y = round(random.uniform(-r,r),2)
    z = round(random.uniform(-r,r),2)
    return (x,y,z)

print("#randPt3 Test")
print (randPt3(10))
print()
# ------------------------------------------------------------------------------
def randSeg2 (r):

##    x1 = random.uniform(-r,r)
##    y1 = random.uniform(-r,r)
##    x2 = random.uniform(-r,r)
##    y2 = random.uniform(-r,r)
##    return [(x1,y1),(x2,y2)]
    return [randPt2(r), randPt2(r)]

print("#randSeg2 Test")
print (randSeg2(10))
print()
# ------------------------------------------------------------------------------
def randTri2 (r):

    return [randPt2(r), randPt2(r), randPt2(r)] 

print("#randTri2 Test")
print (randTri2(10))
print()
# ------------------------------------------------------------------------------
def randCld2_v1 (r, n):

    cloud = []
    for x in range(n):
        cloud.append(randPt2(r))
    return cloud

print("#randCld2_v1 Test")
print (randCld2_v1 (10,5))
print()
# ------------------------------------------------------------------------------
def randCld2_v2 (r, nFirstQuadrant):

    cloud = []
    i = 0
    while i < nFirstQuadrant:
        rp = randPt2(r) 
        cloud.append(rp)
        if rp[0] >= 0 and rp[1] >= 0:
            i+=1
    return cloud

print("#randCld2_v2 Test")
print (randCld2_v2 (10,2))
print()
# ------------------------------------------------------------------------------
def randCld3 (r, n):

    cloud = []
    for x in range(n):
        cloud.append(randPt3(r))
    return cloud

print("#randCld3 Test")
print (randCld3 (10,5))
print()
# ------------------------------------------------------------------------------
def randGaussPt2 (sigma):

    x = random.gauss(0,sigma)
    y = random.gauss(0,sigma)
    return (x,y)

print("#randGaussPt2 Test")
print(randGaussPt2(10))
print()
# ------------------------------------------------------------------------------
def randGaussCld2 (sigma, n):

    cloud = []
    for x in range(n):
        cloud.append(randGaussPt2(sigma))
    return cloud

print("#randGaussCld2 Test")
print(randGaussCld2(10,5))
print()
# ------------------------------------------------------------------------------
def randUnit (r):

    randPt = randPt2(r)
    maga= math.sqrt((randPt[0]**2)+(randPt[1]**2))
    x = randPt[0]/maga
    y = randPt[1]/maga
   
    length2 = math.sqrt((x**2)+(y**2)) #Euclidean distance of random unit vector
    #Print statement below provides the length of the random unit vector,
    #which could be used to verify if it is indeed an unit vector (length of 1)
    """print("[SELF CHECK] Length of randUnit:", length2, .998<=length2<= 1)"""
    
    return (x, y)

print("#randUnit Test")
print(randUnit(10))
print()
# ------------------------------------------------------------------------------
def randCldUnit2 (r,n):

    cloud = []
    for x in range(n):
        cloud.append(randUnit(r))
    return cloud

print("#randCldUnit2 Test")
print(randCldUnit2(10,5))
print()
# ------------------------------------------------------------------------------
