#!/usr/bin/env python3
# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# stack functions
# later, this would be a good example to implement using a class

def push (x,S):
    S.append(x)

def isEmpty (S):
    return len(S) == 0

def pop(S):
    assert not isEmpty(S)
    return S.pop()

def top(S):
    assert not isEmpty(S)
    return S[-1]

def nextToTop(S):
    assert len(S) >= 2
    return S[-2]

S = []
for i in range(1,5):
    push (i,S)
pop(S)
push(5,S)
print(S)
