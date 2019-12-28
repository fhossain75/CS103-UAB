# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# lab 10: a circle class 
import math

class Circle (object):
    # --------------------------------------------------------------------------
    def __init__(self, c, r): 
        
        """The constructor. Create a stack from a list.
        Params: c (int 2-tuple) center
                r (int) radius                  
        """

        self.c = c
        self.r = r
        
    # --------------------------------------------------------------------------
    def area(self):
        
        """Return the area of the circle.

        Returns: (int) area              
        """

        return math.pi * (self.r**2)
    
    # --------------------------------------------------------------------------
    def perimeter(self):

        """Return the perimeter of the circle.

        Returns: (int) perimeter              
        """

        return 2*math.pi*self.r
    
    # --------------------------------------------------------------------------
    def collide(self, c2):
        
        """Detects if the two circles overlap or even touch.
        Params: c1 (int 2-tuple) center of first circle
                r1 (int) radius of first circle
                c2 (int 2-tuple) center of second circle
                r2 (int) radius of second circle
        Returns: (bool) circle collision detection              
        """

        a1 = self.c[0]
        a2 = self.c[0] + self.r
        b1 = d.c[0]
        b2 = d.c[0] + d.r

        c1 = self.c[1]
        c2 = self.c[1] + self.r
        d1 = d.c[1]
        d2 = d.c[1] + d.r
        
        if (b1<=a1<=b2 or d1<=c1<=d2) or (b1<=a2<=b2 or d1<=c2<=d2) or (a1<=b1<=a2 or c1<=d1<=c2) or (a1<=b2<=a2 or c1<=d2<=c2):
            return True
        # I know this is not an elegant aproach, I plan on shortening and making it cleaner later. :)
        elif a1>a2 or b1>b2:
            return False
        else:
            False
    
    # --------------------------------------------------------------------------
    def get_c(self):
        
        """Retrieve the center of the circle.

        Returns: (int 2-tuple) center of the circle              
        """

        return self.c
    
    # --------------------------------------------------------------------------
    def get_r(self):
        
        """Retrieve the radius of the circle.

        Returns: (int) radius of the circle              
        """

        return self.r
    
    # --------------------------------------------------------------------------
    def set_c(self, c):
        
        """Assigns a new center of the circle.
        Params: c (int 2-tuple) center

        Returns: Set the center of the circle              
        """
        
        self.c = c

    # --------------------------------------------------------------------------
    def set_r(self, r):
        
        """Assigns a new radius of the circle.
        Params: r (int) radius
        
        Returns: Set the radius of the circle              
        """

        self.r = r
        
    # --------------------------------------------------------------------------
    def __str__ (self):
        
        """String version of the stack, for printing.

        Returns: (str) a string representation of the set
        """

        return str(self.S)
    
    # --------------------------------------------------------------------------
    def __eq__(self):
        
        """

        Returns:               
        """

        
    # --------------------------------------------------------------------------
    def __lt__(self):

        """

        Returns:               
        """

        
    # --------------------------------------------------------------------------
    def draw(self):

        """

        Returns:              
        """


"""
# some tests to get you started (comment in as you implement methods)
c = Circle ((0,0), 100)
c.draw ('red', True)
c.set_c ((100,0))
c.set_r (50)
c.draw ('blue', False)
d = Circle ((100,0), 10)
if c.collide (d):
    print ('hit')
else:
    print ('miss')
"""
# add more testing

#c = Circle ((0,0), 100)
#print(c.area())
#print(c.r)
#c.set_r(50)
#print(c.get_r())

#d = Circle ((100,0), 10)
#c = Circle ((-6,0), 6)
#d = Circle ((6,0), 8)
c = Circle ((-6,50), 65)
d = Circle ((6,0), 8)
if c.collide (d):
    print ('hit')
else:
    print ('miss')
