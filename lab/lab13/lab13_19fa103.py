#!/usr/bin/env python3
# CS103; john k johnstone; jkj at uab dot edu; mit license

from random import *
################################################################################
# some statistical tools to analyze the quality of your answers
# PLEASE DO NOT CHANGE

def mean(X):
    
    """Mean.
    Params: X (list, either int or float)
    Returns: (float) mean of X
    """

    return sum(X) / len(X)

def variance(X):
    
    """Variance.
    Params: X (list, either int or float)
    Returns: (float) variance of X
    """

    mu = mean(X)
    tot = 0.0
    for x in X:
        tot += (x - mu)**2
    return tot / len(X)
    
def stdDev(X):
    
    """Standard deviation.
    Params: X (list, either int or float)
    Returns: (float) standard deviation of X
    """

    return variance(X)**0.5

################################################################################
def montyDoor (prize, contestant):

    """Find the door Monty will open.

    If there is more than one choice, choose one randomly.
    There will be two choices if contestant correctly chose the prize door.

    Hint: 
    - a set may be handy, but remember that you cannot index a set
    - choice (list ({'tea', 'coffee', 'whiskey'}))) chooses a drink

    Params: 
        prize      (int): the door containing the prize
        contestant (int): the door the contestant chose initially   
    Returns: (int) the door Monty Hall will open (1, 2, or 3)
    """

    #raise NotImplementedError ('montyDoor is a stub')
    doors={1,2,3}
    doors.discard(prize)
    doors.discard(contestant)
    return choice(list(doors))

print("montyDoor Test Calls:")
print(montyDoor(2,1))
print(montyDoor(2,2))
print()

def otherDoor (contestant, monty):

    """Find the door that the contestant could switch to.
    This is the third door: not contestant's door and not Monty's door.

    Hint: a set may be handy

    Params: 
        contestant (int): the door the contestant chose initially
        monty      (int): the door Monty opened
    Returns: (int) the door contestant could switch to
    """
    
    #raise NotImplementedError ('otherDoor is a stub')
    assert contestant!= monty, "Contestant's and monty's doors cannot be the same." 
    doors=[1,2,3]
    doors.remove(contestant)
    doors.remove(monty)
    return doors[0]

print("otherDoor Test Calls:")
#print(otherDoor(2,2)) Assertion test call
print(otherDoor(2,1))
print(otherDoor(2,3))
print()

def experimentMonty (style):
    
    """Monty Hall experiment.

    1. choose the prize door randomly and uniformly over [1,2,3];
    2. choose your door randomly and uniformly over [1,2,3];
    3. Monty chooses the door that is not the prize door and not your door;
    4. figure out the other unopened door
    4. depending on style, switch your door to the other unopened door, or not

    Use printing to debug, and test this function.

    Params: style (int): switching style: 0=never, 1=always, 2=random
    Returns: (bool) did you win the prize?
    """

    #raise NotImplementedError ('experimentMonty is a stub')
    assert style in [0,1,2], "Style must be either 0, 1, or 2."
    #print("Style:",style)
    doors = [1,2,3]
    prize = choice(doors)
    #print("Prize:",prize)
    contestant = choice(doors)
    #print("Contestant:",contestant)
    monty = montyDoor(prize, contestant)
    otherD = otherDoor(contestant, monty)
    if style == 0:
        return bool(contestant == prize)
    elif style == 1:
        #print("otherDoor:",otherD)
        return bool(otherD == prize)
    else:
        #random choice between keeping or switching doors
        return bool(choice([contestant,otherD]) == prize)

print("experimentMonty Test Calls:")
#print(experimentMonty(4)) Assertion test call
print(experimentMonty(0))
print(experimentMonty(1))
print(experimentMonty(2))
print()    

# debug and test the experiment function first
# print (experimentMonty (1))

def trialMonty (style, nExp=1000):
    
    """Run a trial of many experiments, to estimate P(winning prize).

    Hint: this is very similar to code in coinMC.py and pascalMC.py

    Params: 
        style (int): switching style: 0=never, 1=always, 2=random
        nExp  (int): #experiments in this trial
    Returns: (float) probability of winning the prize using this switching style
    """
    
    #raise NotImplementedError ('trialMonty is a stub')
    nWins = 0
    for i in range(nExp):
        if experimentMonty(style):
            nWins +=1
    return nWins/ nExp

print("trialMonty Test Calls:")
print(trialMonty(0))
print(trialMonty(0,10))
print(trialMonty(1))
print(trialMonty(1,10))
print(trialMonty(2))
print(trialMonty(2,10))
print()

def MCMonty (style, nTrial=100, nExp=1000, threshold = .01):
    
    """Run many trials, each yielding an estimate of P(winning prize).

    Hint: this is very similar to code in coinMC.py and pascalMC.py.
    
    Params: 
        style (int): switching style: 0=never, 1=always, 2=random
        nTrial (int): #trials 
        nExp   (int): #experiments per trial
        threshold: (float) stop once s.d. drops below threshold
    Returns: (float) good estimate of P(winning the prize)
    """

    #raise NotImplementedError ('MCMonty is a stub')
    assert threshold > 0
    while True:             # dangerous: let's hope we keep improving the guess!
        est = []
        for i in range(nTrial):
            est.append (trialMonty(style,nExp))
        if stdDev (est) > threshold:
            nTrial *= 2
            nExp *= 2
            print ('Trying again with', nTrial, 'trials')
        else:
            return mean (est)

print("MCMonty Test Calls:")
print(MCMonty(0))
print(MCMonty(1))
print(MCMonty(2))
print()

# after you have debugged the experiment, test and debug the entire simulation:

p_never_switch  = MCMonty (0, 100, 1000, .1)
print ('P(prize) if you never switch = ' + str(p_never_switch) + '\n')

p_always_switch = MCMonty (1, 100, 1000, .1)
print ('P(prize) if you always switch = ' + str(p_always_switch) + '\n')

p_random_switch = MCMonty (2, 100, 1000, .1)
print ('P(prize) if you randomly switch = ' + str(p_random_switch) + '\n')

#Challenge
#Compute the probability of a straight flush (poker hand)
#using Monte Carlo simulation

#40 possible Straight Flushes
