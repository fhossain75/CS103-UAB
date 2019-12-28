# 19fa103; john k johnstone; jkj at uab dot edu; mit license

def argmin (L):

    """Index of the minimum element of a nontrivial list of integers.

    >>> argmin ([42,-3,101,100])
    1

    Params: L (int list) a nontrivial list of integers (len(L) > 0)
    Returns: (int) index of the smallest element
    """
##    assert len(L) > 0
##    m = L[0]
##    for i in range(1, len(L)):
##       if L[i] < m:
##           m = L[i]
##    return L.index(m)

    assert len(L) > 0
    imin = 0
    for i in range(1, len(L)):
        if L[i] < L[imin]:
            imin = i
    return imin

print("Index of Min:", argmin([1,5,3]))
print("Index of Min:", argmin([444,222,777,999]))
print("Index of Min:", argmin([324,145,1345,32,5143,32,33]))

L = [42,-3,101,100]
print (argmin(L))
