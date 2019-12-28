#!/usr/bin/env python3
# CS103; john k johnstone; jkj at uab dot edu; mit license
# massaging Guttag's Figure 16.1 code into our style

import random

################################################################################
# some statistical tools (to analyze the quality of our answers)
# stripping out docstrings, since we have seen this before
def mean(X):
    return sum(X) / len(X)

def variance(X):
    mu = mean(X)
    tot = 0.0
    for x in X:                       # let's show you another way to compute it
        tot += (x - mu)**2
    return tot / len(X)
    
def stdDev(X):
    return variance(X)**0.5
################################################################################
def rollDie():

    """Simulate the random roll of a fair die.
    Returns: (int) the roll
    """
    
    return random.choice([1,2,3,4,5,6])

def experimentPascal ():
    
    """A single experiment of Pascal's problem: roll a pair of die 24 times.
    This is the analogue of the 5 coin flips in earlier simulation.
    Returns: (bool) did double sixes ever pop up?
    """
    
    for j in range(24):
        d1 = rollDie()
        d2 = rollDie()
        if d1 == 6 and d2 == 6:
            return True
    return False

def trialPascal (nExp):

    """Run a trial of many experiments, to estimate P(double 6 in 24 rolls).

       I'm having deja-vu: haven't I seen this code before?

    Params: nExp (int): #experiments in this trial
    Returns: (float) estimated probability P(double 6 in 24 rolls)
    """

    nSuccess = 0
    for i in range(nExp):
        if experimentPascal():
            nSuccess += 1
    return nSuccess / nExp

def MCpascal (nTrial, nExp, threshold):

    """Run many trials, each yielding an estimate of P(double 6 in 24 rolls).

    Am I going crazy?  
    I have another feeling of deja-vu: I could swear I've seen this code before.

    Params: nTrial (int): #trials
            nExp   (int): #experiments per trial
            threshold (float): stop once s.d. drops below threshold
    Returns: (float) good estimate of P(double 6 in 24 rolls)
    """

    assert threshold > 0
    while True:             # dangerous: let's hope we keep improving the guess!
        est = []
        for i in range(nTrial):
            est.append (trialPascal (nExp))
        if stdDev (est) > threshold:
            nTrial *= 2
            nExp *= 2
            print ('Trying again with', nTrial, 'trials')
        else:
            return mean (est)

print ('P(double 6, 24 rolls), analytically:',1-(35/36)**24)
print ('P(double 6, 24 rolls), using Monte Carlo simulation =',
       MCpascal (100, 1000, .1))


