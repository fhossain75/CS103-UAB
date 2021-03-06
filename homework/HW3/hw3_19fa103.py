################################################################################
# HW3, CS103 Fall 2019
# name: Faisal Hossain
# blazerid: faisal75
################################################################################

################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE 'Alan Turing' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Faisal Hossain'
################################################################################

################################################################################
# helper function provided for your use in eApprox: please do not change
import decimal
def significant (d, n):
    """Given a desired precision, express a float to this level of precision.
    >>> significant (12.345678, 4)
    12.35
    Params: 
        d (float): # of interest
        n (int):   precision (# significant digits)
    Returns: (float) d rounded to this precision
    """

    decimal.getcontext().prec = n
    return float(decimal.Decimal(d) / decimal.Decimal (1))
################################################################################

##############
# HW3 PROBLEMS
##############

def eCount (s):

    """Count e's.

    >>> eCount ('Everything is wonderful.')
    3

    Params: s (str)
    Returns: (int) number of e's (either lowercase or uppercase) in s
    """
    ecounter = 0
    for c in s:
        if c == "E" or c=="e":
            ecounter+=1
        else:
            ecounter+=0
    return ecounter

##print(eCount("Faisal is taking Computer Science 103."))
##print(eCount("My cat name is Burberry."))

def pigglyWiggly (w):

    """Translate a word to pig Latin

    >>> pigglyWiggly ('dog')
    'ogday'

    Params: w (str): a single lowercase English word
    Returns: (str) w in pig Latin
    """
    #constant
    if w[0] in "bcdfghjklmnpqrstvxzw":
        return w[1:]+w[0]+"ay"
    #vowel
    if w[0] in "aeiouy":
        return w+"yay"

##print(pigglyWiggly("burberry"))
##print(pigglyWiggly("are"))

def argLongest (L):
    """ Index of the longest even-length string that ends with 'ing'.

    >>> argLongest (['bling', 'loving', 'hating', 'liking'])
    1

    Params: L [string list) len(L) > 0
    Returns: (int) index of longest string of even length that ends with 'ing';
                   if there are many longest strings, choose first that passes
    """
    assert(len(L)>0)
    largest = 0
    longestindex = -1
    for x in L:
        if (len(x)%2==0) and x[-3:] == "ing":
            if len(x) > largest:
                largest = len(x)
                longestindex = L.index(x)
    return(longestindex)

##print(argLongest (['bling', 'loving', 'loving', 'liking', 'yes', 'facts']))

def hurray (n):
    """A string that reveals the structure of the powers of 2.
       See writeup for details.

    >>> hurray (7)
    0hurrayhurray3hurray567

    Params: n (int) n >= 0
    Returns: (str) string of integers 0 through n, inclusive, with every power
                   of 2 replaced by the string 'hurray'
    """
    powersOf2 = []
    start = ""
    for x in range(n+1):
        powersOf2.append(2**x)
    for x in range(n+1):
        if x in powersOf2:
            start+="hurray"
        else:
            start+=str(x)
    return start

##print(hurray(3))
##print(hurray(9))

def eApprox (n):
    """Compute e, up to some accuracy, using Bernoulli's formula.
       (See writeup for details. I will also elaborate in lecture.)

    >>> eApprox (2)
    2.44140625

    Params: n (int) # of significant digits, n >= 1, as defined in writeup
    Returns: (float) in the sequence of approximations of 
                     e generated by Bernoulli's formula, 
                     the later of the first pair of consecutive approximations 
                     that agree to within n significant digits
    """

    return
#Could not attempt due to shortage of time.
#Had two midterms last week and this week, plus tons of homework from other classes.
