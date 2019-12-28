# 19fa103; john k johnstone; jkj at uab dot edu; mit license

import math

def scalarProduct1 (v1, v2, w1, w2):
    """Scalar product in 2 space, using scalars.
    Params:
        v1 (float): x-coordinate of a vector v in 2-space
        v2 (float): y-coordinate of v
        w1 (float): x-coordinate of a vector w in 2-space
        w2 (float): y-coordinate of a vector w
    Returns: (float) v.w
    """
    return v1*w1 + v2*w2

p1="scalarProduct1: "
print ('testing scalarProduct1')
print ("v= (v1,v2) and w= (w1,w2)")
print("v= ({},{}) w = ({},{}) RESULT: {}".format(1.,1,2,3,scalarProduct1(1.,1,2,3)))
print("v= ({},{}) w = ({},{}) RESULT: {}".format(1.,1,2,0,scalarProduct1(1.,1,2,0)))
print("v= ({},{}) w = ({},{}) RESULT: {}".format(1.,1,0,2,scalarProduct1(1.,1,0,2)))
print("v= ({},{}) w = ({},{}) RESULT: {}".format(2.,3,4,5,scalarProduct1(2.,3,4,5)))
# ------------------------------------------------------------------------------
def scalarProduct2 (v,w):
    """Scalar product in 2 space, using tuples.

    >>>scalarProduct2 ((1.,1.), (1.,2.))
    3.0
    
    Params:
        v (tuple): a vector in 2-space
        w (tuple): a vector in 2-space
    Returns: (float) v.w
    """
    return v[0]*w[0] + v[1]*w[1]

print()
print ('testing scalarProduct2')
print("v= ({},{}) w = ({},{}) RESULT: {}".format(1.,1,2,3,scalarProduct2((1.,1),(2,3))))
print("v= ({},{}) w = ({},{}) RESULT: {}".format(1.,1,2,0,scalarProduct2((1.,1),(2,0))))
print("v= ({},{}) w = ({},{}) RESULT: {}".format(1.,1,0,2,scalarProduct2((1.,1),(0,2))))
print("v= ({},{}) w = ({},{}) RESULT: {}".format(2.,3,4,5,scalarProduct2((2.,3),(4,5))))
# ------------------------------------------------------------------------------
def euclideanLength (v):
    """Educlidean length of a vector in 2-space, using a tuple.
    Params:
        v (tuple): a vector in 2-space
    Returns: (float) Euclidean length of v
    """
    return math.sqrt((v[0]**2) + (v[1]**2))

print()
print ('testing euclideanLength')
print (euclideanLength( (1.,1)))
print (euclideanLength( (3.,4)))
print (euclideanLength( (8.,-6)))
# ------------------------------------------------------------------------------
def normalize (v):
    """Normalization of a vector in 2-space, using a tuple.
    Params:
        v (tuple): a vector in 2-space
    Returns: (tuple) Normalization of v
    """
    magnitude = math.sqrt(v[0]**2+v[1]**2)
    return (v[0]/(magnitude),v[1]/(magnitude))

print()
print ('testing normalize')
print (normalize( (3,4) ))
print (normalize( (8,6) ))
print (normalize( (6,8) ))
# ------------------------------------------------------------------------------
def angle (v, w):
    """Angle between two vectors in 2 space, using scalar product.
    Params:
        v (tuple): a vector in 2-space
        w (tuple): a vector in 2-space
    Returns: (float-radian) Angle between v and w.
    """
    return math.degrees(math.acos(scalarProduct2(v,w)/(euclideanLength(v)*euclideanLength(w)))) 

print()
print ('testing angle') 
print (angle ((3,4), (8,6) ))
print (angle ((1,1), (2,3) ))
print (angle ((2,3), (4,5) ))
# ------------------------------------------------------------------------------
def project (v, w):
    """Projection of vector v onto vector w, using scalar product.
    Params:
        v (tuple): a vector in 2-space
        w (tuple): a vector in 2-space
    Returns: (tuple) Projection of v onto w
    """
    unit_w = scalarProduct2(v,w)/euclideanLength(v)**2
    return (unit_w*v[0],unit_w*v[1])

print()
print ('testing project')
print (project ((3,4), (8,6) ))
print (project ((1,1), (2,3) ))
print (project ((2,3), (4,5) ))
