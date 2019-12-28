# 19fa103; john k johnstone; jkj at uab dot edu; mit license

# don't forget your docstrings (the first is provided for you, as an example)
# don't forget your test calls (directly under each function)
# don't forget the body of the function (although that is less likely)

import random

def myMax (L):
    """Maximum element of a nontrivial list of integers.

    >>> myMax ([42, -3, 101, 100])
    101

    Params: L (int list) a nontrivial list of integers (len(L) > 0)
    Returns: (int) the largest element
    """
    assert len(L) > 0
    m = L[0]
    for i in range(1, len(L)):
       if L[i] > m:
           m = L[i]
    return m

print("Max:", myMax([1,4,2,9,3,8]))
print("Max:", myMax([4,67,2,3,12,242]))
print("Max:", myMax([651,435,23,9345,355,854]))
print()
# ------------------------------------------------------------------------------
def myMin (L):
    """Minimum element of a nontrivial list of integers.

    >>> myMin ([42, -3, 101, 100])
    -3

    Params: L (int list) a nontrivial list of integers (len(L) > 0)
    Returns: (int) the smallest element
    """
    assert len(L) > 0
    m = L[0]
    for i in range(1, len(L)):
       if L[i] < m:
           m = L[i]
    return m

print("Min:", myMin([1,4,2,9,3,8]))
print("Min:", myMin([4,67,-2,3,12,242]))
print("Min:", myMin([651,435,23,9345,355,854]))
print()
# -----------------------------------------------------------------------------
def randomListInt (n, a, b):
    """Generate a random list of intergers.

    >>>randomListInt (5, 1, 5)
    [3,5,2,3,4]

    Params:
        n (int): size of random list
        a (int): lowerbound of interval
        b (int): upperbound of interval
    Returns: (int list) a random list of n intergers in the interval
    """
    nab = []
    for i in range(n):
        nab.append(random.randint(a,b))
    return nab

print(randomListInt (5, 1, 5))
print(randomListInt (9, 7, 9))
print(randomListInt (6, 28, 100))
print()
# ------------------------------------------------------------------------------
def argmin (L):
    """Index of the minimum element of a nontrivial list of integers.

    >>> argmin ([42, -3, 101, 100])
    1

    Params: L (int list) a nontrivial list of integers (len(L) > 0)
    Returns: (int) the index of the smallest element
    """
    assert len(L) > 0
    m = L[0]
    for i in range(1, len(L)):
       if L[i] < m:
           m = L[i]
    return L.index(m)

print("Index of Min:", argmin([1,4,2,9,3,8]))
print("Index of Min:", argmin([4,67,2,3,12,242]))
print("Index of Min:", argmin([651,435,235,9345,355,23,854]))


"""
The index of the minimum element is more useful than the minimum element because
it allows you to change the minium element if needed.
"""

""" 
An example of a computation for which the index of the min is useful but the
min is useless is when creating a graph or programming a 3D printer and you
decide to change the minimum value of the graph or the indentation of the object."""
print()
# ------------------------------------------------------------------------------
def argmax (L):
    """Index of the maximum element of a nontrivial list of integers.

    >>> argmax ([42, -3, 101, 100])
    2

    Params: L (int list) a nontrivial list of integers (len(L) > 0)
    Returns: (int) the index of the largest element
    """
    assert len(L) > 0
    m = L[0]
    for i in range(1, len(L)):
       if L[i] > m:
           m = L[i]
    return L.index(m)

print("Index of Max:", argmax([1,4,2,9,3,8]))
print("Index of Max:", argmax([4,67,2,3,12,242]))
print("Index of Max:", argmax([9999,651,435,23,9345,355,854]))
#Only one line and one character (< to >) changes in argmax from argmin.
print()
# ------------------------------------------------------------------------------
print("Test of myMax/myMin/argmin/argmaxfunctions on a randomly generated list")
L = randomListInt(5, -100, 100)
print("Random List:", L)
print("myMax:", myMax(L))
print("myMin:", myMin(L))
print("argmin:", argmin(L))
print("argmax:", argmax(L))
print()
# ------------------------------------------------------------------------------
def randomListFloat1 (n):
    """Generate a random list of floats.

    >>>randomListFloat1 (3)
    [0.14, 0.50, 0.36]

    Params:
        n (int): size of random list
    Returns: (float list) a random list of n floats in the interval
    """
    nf1 = []
    for i in range(n):
        nf1.append(random.random())
    return nf1
print(randomListFloat1 (3))
print(randomListFloat1 (4))
print(randomListFloat1 (5))
print()
# ------------------------------------------------------------------------------
def randomListFloat2 (n, a, b):
    """Generate a random list of floats.

    >>>randomListFloat1 (3,-10,10)
    [-3.55, 5.19, -0.60]

    Params:
        n (int): size of random list
        a (int): lowerbound of interval
        b (int): upperbound of interval
    Returns: (float list) a random list of n intergers in the interval
    """
    nf2 = []
    for i in range(n):
        nf2.append(random.uniform(a,b))
    return nf2
print(randomListFloat2 (3,-10,10))
print(randomListFloat2 (4,2,4))
print(randomListFloat2 (5,0,10))
print()
# ------------------------------------------------------------------------------
print("Challenges")
def randomListString (n):
    """Generate a random list of strings.

    >>>randomListString (5)
    [0.14, 0.50, 0.36]

    Params:
    n (int): size of random list
    Returns: (float list) a random list of n floats in the interval
    """
    ns = []
    abc="abcdefghijklmnopqrstuvwxy"
    t=""

##    for c in range(n):
##        t = t + random.choice(abc)
##    return t
    for d in range(n):
        for c in range(n):
            t = random.choice(abc) + t
        ns.append(t)
    return ns

print(randomListString (3))
print()
