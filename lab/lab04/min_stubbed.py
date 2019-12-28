# 19fa103; john k johnstone; jkj at uab dot edu; mit license

def myMin (L):

    """Minimum element of a nontrivial list of integers.

    >>> myMin ([42, -3, 101, 100])
    -3

    Params: L (int list) a nontrivial list of integers (len(L) > 0)
    Returns: (int) the smallest element
    """

    return

L = [42, -3, 101, 100]
print ('myMin:       ', myMin(L))

# compare against a known correct answer, using the built-in function `min`
print ('built-in min:', min(L))
