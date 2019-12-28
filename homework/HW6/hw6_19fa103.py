################################################################################
# HW6 CS103 Fall 2019

# I declare that I have completed this assignment completely and entirely
# on my own, without any consultation with others.
# I also declare that I have not used internet resources or physical books
# to help with this assignment, except for non-coding mathematical literature
# to help understand the computational approach to these questions.
# I have read the UAB Academic Honor Code and understand that any breach
# of the Honor Code may result in severe penalties.

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
import math

# Helper Functions

def euclideanDistance (v1,v2):
    """Educlidean distance of two vectors in 2-space, using a tuple.
    Params:
        v1 (tuple): a vector in 2-space
        v2 (tuple): a vector in 2-space
    Returns: (float) Euclidean distance of v1 and v2
    """
    
    return math.sqrt( ((v2[0]-v1[0])**2) + ((v2[1]-v1[1])**2) )

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

def euclideanLength (v):
    """Educlidean length of a vector in 2-space, using a tuple.
    Params:
        v (tuple): a vector in 2-space
    Returns: (float) Euclidean length of v
    """
    return math.sqrt((v[0]**2) + (v[1]**2))

################################################################################

class Pol (object):
    
    """Pol is a closed polygon in 2-space."""

    def __init__ (self, vtx):
        
        """Initialize a closed polygon from a list of vertices.
        Params: vtx (list of float 2-tuples) vertices, ordered around the bdry
        """
        self.vtx = vtx

    def __str__ (self):

        """str method
        Returns: (str) a string representation of the polygon
        """
        return str(self.vtx)

    def perimeter (self):
        
        """Sum of the lengths of the sides of the polygon.
        Returns: (float) perimeter
        """
        vtxLens = []
        for x in range(len(self.vtx)-1):
            vtxLens.append(euclideanDistance(self.vtx[x],self.vtx[x+1]))
        vtxLens.append(euclideanDistance(self.vtx[0],self.vtx[-1]))
        
        return sum(vtxLens)
        
    def avgEdgeLength (self):

        """
        Returns: (float) average edge length
        """
        return self.perimeter()/len(self.vtx)

    def angle (self, i):

        """
        Params: i (int): vertex index (0 = first vertex)
        Returns: (float) angle, in degrees, at vertex i
        """
        self.i = i
        vtx = self.vtx
        
        if i == 0:
            eD1 = euclideanDistance (vtx[i],vtx[-1])
            s1 = (vtx[-1][0]-vtx[i][0],vtx[-1][1]-vtx[i][1])
        else:
            eD1 = euclideanDistance (vtx[i],vtx[i-1])
            s1 = (vtx[i-1][0]-vtx[i][0],vtx[i-1][1]-vtx[i][1])
            
        eD2 = euclideanDistance (vtx[i],vtx[i+1])
        s2 = (vtx[i+1][0]-vtx[i][0],vtx[i+1][1]-vtx[i][1])

        return math.degrees(math.acos(scalarProduct2(s1,s2)/(eD1*eD2))) 

    def isSimple (self):                                        # optional bonus

        """Test for simplicity.
        A polygon is simple if it has no self-intersections.
        That is, non-neighbouring edges do not intersect.
        Returns: (bool) is this polygon simple?
        """
        vtx = self.vtx
        isSimpleCheck= None
        
        for x in range(len(vtx)-1):
            a1= vtx[x][0]
            a2= vtx[x][1]
            if x ==2:
                b1= vtx[0][0]
                b2= vtx[0][1]
            else:
                b1= vtx[x+1][0]
                b2= vtx[x+1][1]
            
            if b1<=a1<=b2 or b1<=a2<=b2 or a1<=b1<=a2 or a1<=b2<=a2:
                return True
            elif a1>a2 or b1>b2:
                return False
            else:
                return False             

    def isConvex (self):                                        # optional bonus

        """Test for convexity.

        A set S is convex if A, B in S implies the line segment AB is in S.
        But can you make this computational?
        Hint: the cross product is your friend.

        Returns (bool) is this polygon convex?
        """
        pass

class Tri (Pol):

    """Tri is a triangle class."""

    def __init__ (self, A, B, C, rgbA, rgbB, rgbC):
        
        """
        Params:
            A,B,C (float 2-tuples): vertices of the triangle ABC
            rgbA, rgbB, rgbC (int 3-tuples): RGB colours of the vertices
                     colour range is [0,255]; e.g., 0 <= rgbA[i] <= 255
        """
        self.A = A
        self.B = B
        self.C = C
        self.rgbA = rgbA
        self.rgbB = rgbB
        self.rgbC = rgbC

    def __str__ (self):

        """
        Returns: (str) a string representation of the triangle
        """
        return str([self.A,self.B,self.C])
    
    def getColour (self, i):

        """
        Params: i (int): vertex index, 0<=i<=2
        Returns: (int 3-tuple) colour of ith vertex
        """
        self.i = i
        A= self.A
        B= self.B
        C= self.C
        rgbA= self.rgbA
        rgbB= self.rgbB
        rgbC= self.rgbC
        
        vtx = [[A,rgbA], [B,rgbB], [C,rgbC]]

        return vtx[i][1]

    def isEquilateral (self, eps):

        """Test for equilateral triangle.
        Params: eps (float): allowable deviation in length
        Returns: (bool) is the triangle equilateral within eps?
                        (difference between min edge and max edge < eps?)
        """
        self.eps = eps
        A= self.A
        B= self.B
        C= self.C
        
        vtx = [A,B,C]
        vtxLens = []
        for x in range(len(vtx)-1):
            vtxLens.append(euclideanDistance(vtx[x],vtx[x+1]))
        vtxLens.append(euclideanDistance(vtx[0],vtx[-1]))

        return (min(vtxLens) - max(vtxLens)) < eps
        
    def signedArea (self):

        """
        Returns: (float) signed area of the triangle, +ve iff counterclockwise
        """
        #Heron's Formula
        a= euclideanDistance(self.A,self.B) #side length of AB
        b= euclideanDistance(self.B,self.C) #side length of BC
        c= euclideanDistance(self.C,self.A) #side length of CA
        s = (a+b+c)/2 #semi-perimeter of the triangle

        return math.sqrt(s*(s-a)*(s-b)*(s-c))

    def angle (self, i):

        """
        Params: i (int): vertex index (0 = first vertex)
        Returns: (float) angle, in degrees, at vertex i
        """
        self.i = i
        A= self.A
        B= self.B
        C= self.C
        vtx = [A,B,C]
        
        if i == 0:
            eD1 = euclideanDistance (vtx[i],vtx[-1])
            s1 = (vtx[-1][0]-vtx[i][0],vtx[-1][1]-vtx[i][1])
        else:
            eD1 = euclideanDistance (vtx[i],vtx[i-1])
            s1 = (vtx[i-1][0]-vtx[i][0],vtx[i-1][1]-vtx[i][1])

        if i == 2:
            eD2 = euclideanDistance (vtx[i],vtx[0])
            s2 = (vtx[0][0]-vtx[i][0],vtx[0][1]-vtx[i][1])
        else:
            eD2 = euclideanDistance (vtx[i],vtx[i+1])
            s2 = (vtx[i+1][0]-vtx[i][0],vtx[i+1][1]-vtx[i][1])

        return math.degrees(math.acos(scalarProduct2(s1,s2)/(eD1*eD2)))
    
    def perimeter (self):
        
        """Sum of the lengths of the sides of the polygon.
        Returns: (float) perimeter
        """
        A= self.A
        B= self.B
        C= self.C
        vtx = [A,B,C]
        vtxLens = []
        for x in range(len(vtx)-1):
            vtxLens.append(euclideanDistance(vtx[x],vtx[x+1]))
        vtxLens.append(euclideanDistance(vtx[0],vtx[-1]))
        
        return sum(vtxLens)
        
    def avgEdgeLength (self):

        """
        Returns: (float) average edge length
        """

        return self.perimeter()/3

    def isCCW (self):
        
        """Counterclockwise orientation.
        ccw iff all (both) turns are left
        Returns: (bool) is the triangle oriented counterclockwise?
        """
        pass
        
    def centroid (self):                                        # optional bonus

        """
        Returns: (float 2-tuple): centroid of the triangle
        """
        A= self.A
        B= self.B
        C= self.C

        return ((A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3)

    def circumCenter (self):                                    # optional bonus

        """Circumcenter, the center of the circumscribing circle.
        Returns: (float 2-tuple): circumcenter of the triangle
        """
        A= self.A
        B= self.B
        C= self.C
        a= self.angle(0) #angle of A
        b= self.angle(1) #angle of B
        c= self.angle(2) #angle of C
        div = (math.sin(2*a)+math.sin(2*b)+math.sin(2*c))

        cX = (((A[0]*math.sin(2*a))+(B[0]*math.sin(2*b))+(C[0]*math.sin(2*c)))/div)
        cY = (((A[1]*math.sin(2*a))+(B[1]*math.sin(2*b))+(C[1]*math.sin(2*c)))/div)

        return (cX,cY)

