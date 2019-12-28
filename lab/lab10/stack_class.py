# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# note how the methods imitate the stack functions we built earlier;
# note the difference in how we call these functions (bottom of script)
# notice that it is a bit more complicated inside the method,
# but a bit simpler when used outside

def lint (L):

    """Is L a list of integers?  Solved recursively.
    Params: L (list)
    Returns: is every element of L an integer?
    """

    assert type(L) == list
    if L == []:                  # base case: if empty, every elt is an integer!
        return True
    elif type(L[0]) != int:      # base case: if first elt is not, list is not
        return False
    else:
        return lint(L[1:])       # recursive call: first passes, does rest?

# ------------------------------------------------------------------------------
class Stack(object):         # integer stack, represented internally by a list S
    # --------------------------------------------------------------------------
    def __init__(self, L=[]): 
        
        """The constructor. Create a stack from a list.
        Params: L (int list) the initial contents of the stack (default: empty)
                             last element of the list is the top of the stack;
        """

        assert lint(L)                                      # guard the entrance
        self.S = L

    # --------------------------------------------------------------------------
    def isEmpty (self):
 
        """Test the status of the stack.

        Returns: (bool) is the stack empty?
        """

        return len(self.S) == 0

    # --------------------------------------------------------------------------
    def push (self, x):

        """Push an element on the top of the stack.

        Params: x (int)
        """

        self.S.append (x)

    # --------------------------------------------------------------------------
    def pop (self):

        """Pop off the top element.

        Returns: (int) top element
        """

        assert not self.isEmpty()
        return self.S.pop()

    # --------------------------------------------------------------------------
    def top (self):

        """Return the top element, without popping it.

        Redundant since it could be simulated by 
        x = S.pop()
        S.push(x)
        but added since it is a common operation.

        Returns: (int) top element
        """

        assert not self.isEmpty ()
        return self.S[-1]

    # --------------------------------------------------------------------------
    def __str__ (self):
        
        """String version of the stack, for printing.

        Returns: (str) a string representation of the set
        """

        return str(self.S)

S = Stack ()                              # calls __init__
assert S.isEmpty()
for i in range(1,5):
    print ("pushing " + str(i))
    S.push (i)
print ('popping')    
S.pop()
print ('pushing 5')
S.push(5)
print ('top element is ' + str(S.top()))
print ('present status of stack: ')
print(S)                                  # calls __str__

# ------------------------------------------------------------------------------

T = Stack ([1,2,3,6])
print ('a second stack')
print (T)

# exercise: test equality of S and T
"""
if S == T:
    print ('the two stacks are identical')
else:
    print ('the two stacks differ')

T = Stack ([1,2,3,5])

if S == T:
    print ('the two stacks are identical')
else:
    print ('the two stacks differ')
"""
