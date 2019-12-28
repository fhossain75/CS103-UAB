# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# lab07 tests, written for you this time

from lab07_19fa103 import *
# ------------------------------------------------------------------------------
# pay no attention to the man behind the curtain
def prettyPrint (L):

    """Prettyprint a list. (I could be even prettier.)
    Params: L (list)
    """

    assert type(L) == list
    assert len(L) >= 2                 # to guard the first and last print
    print ('  [', end='')
    print (' ' + str(L[0]) + ',')    # I'm special, I'm short
    for i in range(1,len(L)-1):
        print ('    ' + str(L[i]) + ',')
    print ('    ' + str(L[-1]) + ' ]')
# ------------------------------------------------------------------------------
p = randPt2 (100)
if p != None:
    print ('random point: ' + str(p))

p = randSeg2 (100)
if p != None:
    print ('random segment:')
    prettyPrint (p)

p = randTri2 (100)
if p != None:
    print ('random triangle:')
    prettyPrint (p)

p = randCld2_v1 (100, 4)
if p != None:
    print ('random point cloud:')
    prettyPrint (p)

p = randCld2_v2 (100, 4)
if p != None:
    print ('random point cloud, with control over first quadrant:')
    prettyPrint (p)

p = randCld3 (100, 4)
if p != None:
    print ('random point cloud in 3-space:')
    prettyPrint (p)

p = randGaussPt2 (50)
if p != None:
    print ('random Gaussian point: ' + str(p))

p = randGaussCld2 (50, 4)
if p != None:
    print ('random point cloud sampled from Gaussian distribution:')
    prettyPrint (p)

p = randUnit ()
if p != None:
    print ('random unit vector: ' + str(p))

p = randCldUnit2 (4)
if p != None:
    print ('random set of unit vectors:')
    prettyPrint (p)
