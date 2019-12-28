# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# lab08 on recursion

# ------------------------------------------------------------------------------
def sum (n):

    assert n >= 1
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

# ------------------------------------------------------------------------------
def reverse1 (s):

    assert len(s) >= 1
    if len(s) == 1:
        return s
    else:
        return reverse1(s[1:]) + s[0]

# ------------------------------------------------------------------------------
# use another way to implement it recursively
def reverse2 (s):

    return
# ------------------------------------------------------------------------------
def sumMtoN (M, N):

    assert M <= N
    if N == M:
        return M
    else:
        return N + sumMtoN(M, N-1)

# ------------------------------------------------------------------------------
def lint (L):

    return

# ------------------------------------------------------------------------------
def argmax (L):

    return
