# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# collecting all our early examples of incremental functions using a for loop,
# to illustrate the common structure:
#
# - initialize the value
# – for each element
#     - process the element to update the value
# – return the value
#
# removing docstrings so that the code jumps out

def sp (v,w):                                                   # scalar product
    s = 0
    for i in range(len(v)):
        s += v[i]*w[i]
    return s

def reverse1 (s):                                              # string reversal
    t = ''
    for c in s:
        t = c + t
    return t

# ------------------------------------------------------------------------------
def reverse2 (s):                                              # string reversal
    t = ''
    for i in range(len(s)):
        t = s[i] + t
    return t

# ------------------------------------------------------------------------------
def reverse3 (s):                                              # string reversal
    t = ''
    for i in range(len(s)-1, -1, -1):
        t = t + s[i]
    return t

def myMin (L):                                                 # min of int list

    assert len(L) > 0
    m = L[0]
    for i in range(1,len(L)):
        if L[i] < m:
            m = L[i]
    return m

def argmin (L):

    assert len(L) > 0
    imin = 0
    for i in range(1,len(L)):
        if L[i] < L[imin]:
            imin = i
    return imin

