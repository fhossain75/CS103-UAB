# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# lab08 on recursion

# ------------------------------------------------------------------------------
def sum (n):
    
    """Compute the sum of the first n positive integers, recursively.

    >>> sum (10)
    55

    Params: n (int) n >= 1
    Returns: (int) sum from 1 to n (1 + 2 + ... + n)
    """
    assert n >= 1
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

print(sum(10))
print(sum(5))
# ------------------------------------------------------------------------------
def reverse1 (s):

    """Reverse a string, recursively.

    >>> reverse ('garden')
    nedrag

    Params: s (str) 
    Returns: (str) reversal of s
    """
    assert len(s) >= 1
    if len(s) == 1:
        return s
    else:
        return reverse1(s[1:]) + s[0]
    
print(reverse1("garden"))
# ------------------------------------------------------------------------------
# use another way to implement it recursively
def reverse2 (s):

    """Reverse a string, recursively.

    >>> reverse ('garden')
    nedrag

    Params: s (str) 
    Returns: (str) reversal of s
    """
    
    return
# ------------------------------------------------------------------------------
def sumMtoN (M, N):

    """Recursive sum from M to N.
    Params: 
        M (int): 
        N (int): M <= N
    Returns: M + ... + N
    """
    assert M <= N
    if N == M:
        return M
    else:
        return N + sumMtoN(M, N-1)
    
print(sumMtoN(0, 3))
print(sumMtoN(2, 3))
print(sumMtoN(0, 10))
# ------------------------------------------------------------------------------
def lint (L):

    """Is L a list of integers?  Solved recursively.

    >>> lint ([0, 2, 3.1, 'joe'])
    False
    >>> lint ([123, 234, 345])
    True

    Params: L (list)
    Returns: is every element of L an integer?
    """

    return

# ------------------------------------------------------------------------------
def argmax (L):

    """Index of the max element of a nontrivial list of integers, recursively.

    >>> argmax ([42,-3,101,100])
    2

    Params: L (int list) a nontrivial list of integers (len(L) > 0)
    Returns: (int) index of the largest element (first if many ties);
                   use a nonnegative index
    """

    return
