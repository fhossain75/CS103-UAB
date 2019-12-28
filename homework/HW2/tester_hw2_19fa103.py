# 19fa103 Johnstone
# HW2 tester: please do not change
# python3; copyright 2019 john k johnstone jkj at uab dot edu ; mit license

# check for syntax errors in the submission
print ("Checking for syntax errors ...", end='')
try:
    import hw2_19fa103                                  # the student's homework
except Exception as e:
    print ()
    print ('Your code contains a syntax error. Please correct and resubmit.')
    print (e)
    exit (1)
print ('passed')

########################################################################
### enforce HW2 constraints on syntax and style, for each fn
########################################################################

import inspect
from tokenize import tokenize
from io import BytesIO

def lint_103 (code, banned_tokens):
    """Ban certain tokens (e.g., later syntax) and enforce 80-column lines.
    Params: 
        code (str): code to be linted
        banned_tokens (list of strings): the banned tokens
    """

    assert (type(banned_tokens) == list)

    # ban certain tokens
    s = code
    g = tokenize (BytesIO (s.encode ('utf-8')).readline)
    for toknum, tokval, _, _, _ in g:
        # ignore empty tokens and whitespace tokens (which do oddly arise)
        if not tokval.strip() == "" and tokval in banned_tokens:
            print ('\nDisallowed token: "' + tokval + '"')
            print ("You are using a feature of Python that is not allowed " +\
                    "in this assignment.\nYou will need to solve this " +\
                    "assignment without using that feature.")
            exit(1)

    # ban long lines
    t = code
    L = t.splitlines()
    for line in L:
        if (len(line) > 80):
            print ('\nDisallowed line: ' + str(line))
            print ("You may not have a line of code longer than 80 characters.")
            exit(1)

banned_tokens_hw2 = (
    'print,numpy,hypot,binom,' + 
    'for,while,str,string,in,is,len,list,range,' +
    'break,class,continue,dict,eval,except,filter,finally,global,hex,' +
    '__import__,lambda,map,open,set,slice,try,tuple,input,raise,' + 
    'repr,with,yield,[,],{,}')
banned_tokens = banned_tokens_hw2.split(',')
print ("Checking for violations of CS103 HW2 syntax constraints...", end='')
lint_103 (inspect.getsource (hw2_19fa103), banned_tokens)
print ("passed\n")

import random

# ------------------------------------------------------------------------------
# motivation: you should never expect two floats to be exactly equal
# because of machine precision (more later in lecture)

def approxEq (a,b,eps=.00001):  # the 3rd parameter is given a default value
    """Is a ~ b?
    >>> approxEq (1, 1.000001, .0001)
    True
    Params: 
        a: (float)
        b: (float)
        eps: (float) allowable difference
    Returns: (bool) is a within eps of b?
    """
    
    return abs(a-b) < eps

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

# ------------------------------------------------------------------------------
def grade (test_id, answer, correct_answer):
    """Grade an answer.
    Params:
        test_number (str): ID of the test
        answer (flexible type): submitted answer
        correct_answer (same type as answer): correct answer
    Returns: (bool) is answer correct?
    """
    
    if answer != None:
        print (test_id + ' should be ' + str(correct_answer), end='')
        print ('. Your answer: '+str(answer), end='  ')
    typeCorrect = type(answer) == type(correct_answer)
    if answer != None and typeCorrect and answer == correct_answer:
        print ('CORRECT')
        return True
    else:
        print ('WRONG')
        return False

def gradeApprox (test_id, answer, correct_answer):
    """Grade an answer.
    Params:
        test_number (str): ID of the test
        answer (float): submitted answer
        correct_answer (float): correct answer
    Returns: (bool) is answer correct?
    """
    
    if answer != None:
        print (test_id + ' should be about ', end='')
        print (str (significant (correct_answer, 7)), end='')
        print ('. Your answer: ', end='')
        print (str (significant (answer, 7)), end='  ')
    if answer != None and approxEq (answer, correct_answer):
        print ('CORRECT')
        return True
    else:
        print ('WRONG')
        return False

################################################################################
################################################################################
################################################################################
from hw2_19fa103 import *

def testP ():
    print ('Testing p.')
    nCorrect = 0
    if gradeApprox ('pre0', p (0.), 1):
        nCorrect += 1
    if gradeApprox ('pre1', p (1.), 1):
        nCorrect += 1
    if gradeApprox ('pre2', p (-1.), 0):
        nCorrect += 1
    if gradeApprox ('pre3', p (11.5), 0):
        nCorrect += 1
    print ()
    return nCorrect == 4

def testIsOdd ():
    print ('Testing isOdd.')
    nCorrect = 0
    if grade ('t1', isOdd (5), True):
        nCorrect += 1
    if grade ('t2', isOdd (42), False):
        nCorrect += 1
    if grade ('t3', isOdd (-101), True):
        nCorrect += 1
    if grade ('t4', isOdd ('hi'), False):
        nCorrect += 1
    if grade ('t5', isOdd ('3.14159'), False):
        nCorrect += 1
    print ()
    return nCorrect == 5
    
def testInAWhile ():
    print ("Testing inAWhile.")
    nCorrect = 0
    if grade ('t6', inAWhile (2, 3), 5):
        nCorrect += 1
    if grade ('t7', inAWhile (1, 12), 1):
        nCorrect += 1
    if grade ('t8', inAWhile (1, 48), 1):
        nCorrect += 1
    if grade ('t9', inAWhile (12, 1), 1):
        nCorrect += 1
    if grade ('t10', inAWhile (12, -23), 1):
        nCorrect += 1
    if grade ('t11', inAWhile (12, 0), 12): # !
        nCorrect += 1        
    if grade ('t12', inAWhile (12, 1), 1):
        nCorrect += 1
    if grade ('t13', inAWhile (5, 7), 12):  # !
        nCorrect += 1    

    try:
        inAWhile (5.1, 7)
    except AssertionError:
        print ('CORRECT')
        nCorrect += 1
    else:
        print ("WRONG: a parameter fails the constraints: check for this.")

    try:
        inAWhile (5, 7.)
    except AssertionError:
        print ('CORRECT')
        nCorrect += 1
    else:
        print ("WRONG: a parameter fails the constraints: check for this.")

    print()
    return nCorrect == 10

def testPixelLuminance ():
    print ("Testing pixelLuminance.")
    nCorrect = 0
    if grade ('t14', pixelLuminance (100, 50, 250), 75):
        nCorrect += 1
    if grade ('t15', pixelLuminance (255, 10, 10), 62):
        nCorrect += 1
    if grade ('t16', pixelLuminance (10, 255, 10), 185):
        nCorrect += 1
    try:
        pixelLuminance (-1, 0, 0)
        nCorrect += 1
    except AssertionError:
        print ('CORRECT')
        nCorrect += 1
    else:
        print ("WRONG: a parameter fails the constraints: check for this.")
    try:
        pixelLuminance (0, 256, 0)
        nCorrect += 1
    except AssertionError:
        print ('CORRECT')
        nCorrect += 1
    else:
        print ("WRONG: a parameter fails the constraints: check for this.")
    try:
        pixelLuminance (1.5, 0, 0)
        nCorrect += 1
    except AssertionError:
        print ('CORRECT')
        nCorrect += 1
    else:
        print ("WRONG: a parameter fails the constraints: check for this.")
    print()
    return nCorrect == 6

def testIOverlap (): # warning: these tests do not exhaustively cover the cases
    print ('Testing iOverlap.')
    nCorrect = 0
    if grade ('t17', iOverlap (-54.23, -17.67, 29.46, 64.48), False):
        nCorrect += 1
    if grade ('t18', iOverlap (-97.14, -27.24, -51.61, 24.01), True):
        nCorrect += 1
    if grade ('t19', iOverlap (-4.01, 67.55, -1.186, 5.423), True):
        nCorrect += 1
    print ()
    return nCorrect == 3

def testIOverlapLen (): # warning: ditto
    print ('Testing iOverlapLen.')
    nCorrect = 0
    if gradeApprox ('t20', iOverlapLen (-54.23, -17.67, 29.46, 64.48), 0.0):
        nCorrect += 1
    if gradeApprox ('t21', iOverlapLen (-97.14, -27.24, -51.61, 24.01), 24.37):
        nCorrect += 1
    if gradeApprox ('t22', iOverlapLen (-4.01, 67.55, -1.186, 5.423), 6.609):
        nCorrect += 1
    print ()
    return nCorrect == 3

def testROverlap (): # warning: ditto
    print ('Testing rOverlap.')
    nCorrect = 0
    answer = rOverlap (-92.12, -59.73, 78.69, 86.04, -83.8, -92.42,106.0,132.2)
    if grade ('t23', answer, True):
        nCorrect += 1
    answer = rOverlap (29.66, 39.19, 49.64, 53.93, -1.794, 23.26, 26.57, 33.46)
    if grade ('t24', answer, False):
        nCorrect += 1
    answer = rOverlap (-74.87,-32.55,67.78,81.93,-76.41,-11.66,44.02,33.33)
    if grade ('t25', answer, True):
        nCorrect += 1
    print ()
    return nCorrect == 3
    
def testROverlapArea ():
    print ('Testing rOverlapArea.')
    nCorrect = 0
    answer = rOverlapArea (-92.12,-59.73,78.69,86.04,-83.8,-92.42,106.0,132.2)
    if gradeApprox ('t26', answer, 6054.6348):
        nCorrect += 1
    answer = rOverlapArea (29.66,39.19,49.64,53.93,-1.794,23.26,26.57,33.46)
    if gradeApprox ('t27', answer, 0.0):
        nCorrect += 1
    answer = rOverlapArea (-74.87,-32.55,67.78,81.93,-76.41,-11.66,44.02,33.33)
    if gradeApprox ('t28', answer, 1415.8584):
        nCorrect += 1
    print ()
    return nCorrect == 3

########################################
# HW2 main
########################################

def testAll():
    print ('Hello, ' + myName() + '. (If this is not your name, fix myName.)')
    print ('Commencing unit tests...')
    nCorrectQ = 0
    if testP ():
        nCorrectQ += 1
    if testIsOdd ():
        nCorrectQ += 1
    if testInAWhile ():
        nCorrectQ += 1
    if testPixelLuminance ():
        nCorrectQ += 1
    if testIOverlap ():
        nCorrectQ += 1
    if testIOverlapLen ():
        nCorrectQ += 1
    if testROverlap ():
        nCorrectQ += 1
    if testROverlapArea ():
        nCorrectQ += 1
    print ('# questions correct: ' + str(nCorrectQ) + ' out of 8')
    print ('Note that passing this tester is a positive sign, ')
    print ('but not a guarantee that your code is correct.')
    print ('You should test it yourself too.')
    
def main():
    testAll()

if __name__ == '__main__':
    main()
