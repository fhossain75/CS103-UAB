# 19fa103; john k johnstone; jkj at uab dot edu; mit license
# HW4 tester: please do not change; feel free to look it over

print ("Use this tester to help refine your code.")
print ("But do not become overly dependent on it. Test the code yourself too.")
       
# check for syntax errors in the submission
print ("Checking for syntax errors ...", end='')
try:
    import hw3_19fa103                                  # the student's homework
except Exception as e:
    print ()
    print ('Your code contains a syntax error. Please correct and resubmit.')
    print ('For a fuller error message, ',end='')
    print ('run your code using `python hw3_19fa103.py`.')
    print (e)
    exit (1)
print ('passed')

########################################################################
### enforce HW3 constraints on syntax and style, for each fn
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

banned_tokens_hw3 = (
    'print,count,argmin,argmax,min,max,numpy,sort,' +
    'class,dict,eval,except,filter,finally,global,hex,' +
    '__import__,map,open,set,slice,try,tuple,raise,' + 
    'repr,with,yield')
banned_tokens = banned_tokens_hw3.split(',')
print ("Checking for violations of CS103 HW3 syntax constraints...", end='')
lint_103 (inspect.getsource (hw3_19fa103), banned_tokens)
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

def ApproxEqualPt (P, Q, eps=.001):
    # are two points in 2-space approximately equal? i.e., dist(P,Q) < eps
    d = np.linalg.norm (np.array(Q) - np.array(P))
    # print ("distance =", d) # to discover what a good tolerance is
    return d < eps

def gradeApproxTuple (test_id, answer, correct_answer):
    """Grade an answer.
    Params:
        test_number (str): ID of the test
        answer (float): submitted answer
        correct_answer (float): correct answer
    Returns: (bool) is answer correct?
    """
    
    if answer != None:
        print (test_id + ' should be about ', end='')
        print (str ((significant (correct_answer[0], 7), 
                     significant (correct_answer[1], 7))), end='')
        print ('. Your answer: ', end='')
        print (str ((significant (answer[0], 7), 
                     significant (answer[1], 7))), end=' ')
    if answer != None and ApproxEqualPt (answer, correct_answer):
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
from hw3_19fa103 import *

def testECount ():
    print ('Testing eCount.')
    nCorrect = 0
    if grade ('t1', eCount ('Every e please.'), 5):
        nCorrect += 1
    if grade ('t2', eCount ('everyone'), 3):
        nCorrect += 1
    if grade ('t3', eCount ('To be or not to be, that is the question.'), 4):
        nCorrect += 1
    if grade ('t4', eCount ('nothing at all'), 0):
        nCorrect += 1
    print()
    return nCorrect == 4

def testPigglyWiggly ():
    print ('Testing pigglyWiggly.')
    nCorrect = 0
    if grade ('t5', pigglyWiggly ('dog'), 'ogday'):
        nCorrect += 1
    if grade ('t6', pigglyWiggly ('cat'), 'atcay'):
        nCorrect += 1
    if grade ('t7', pigglyWiggly ('each'), 'eachyay'):
        nCorrect += 1
    if grade ('t8', pigglyWiggly ('every'), 'everyyay'):
        nCorrect += 1
    print()
    return nCorrect == 4

def testArgLongest ():
    print ('Testing argLongest.')
    nCorrect = 0
    if grade ('t9', argLongest (['bling', 'loving', 'hating', 'liking']), 
              1):
        nCorrect += 1
    if grade ('t10', argLongest (['jewelry', 'bling', 'necklace']),
              -1):
        nCorrect += 1
    if grade ('t11', 
              argLongest(['walking','running','jogging','attempting']),
              3):
        nCorrect += 1
    print()
    return nCorrect == 3

def testHurray ():
    print ('Testing hurray.')
    nCorrect = 0
    if grade ('t15', hurray (5), 
              '0hurrayhurray3hurray5'):
        nCorrect += 1
    if grade ('t16', hurray (10), 
              '0hurrayhurray3hurray567hurray910'):
        nCorrect += 1
    if grade ('t17', hurray (16), 
              '0hurrayhurray3hurray567hurray9101112131415hurray'):
        nCorrect += 1
    print()
    return nCorrect == 3

# yes, we need *exact* equality even though float!
def testEApprox ():
    print ('Testing eApprox.')
    nCorrect = 0
    if grade ('t12', eApprox (1), 2.25):
        nCorrect += 1
    if grade ('t13', eApprox (2), 2.44140625):
        nCorrect += 1
    if grade ('t14', eApprox (3), 2.6328787177279187):
        nCorrect += 1
    print()
    return nCorrect == 3

########################################
# HW3 main
########################################

def testAll():
    print ('Hello, ' + myName() + '. (If this is not your name, fix myName.)')
    print ('Commencing unit tests...')
    nCorrectQ = 0         # where `correct` doesn't necessarily mean correct ...
    if testECount():
        nCorrectQ += 1
    if testPigglyWiggly():
        nCorrectQ += 1
    if testArgLongest():
        nCorrectQ += 1
    if testHurray():
        nCorrectQ += 1
    if testEApprox():
        nCorrectQ += 1
    print ('# questions passed the tester: ' + str(nCorrectQ) + ' out of 5')
    print ('Note that passing the tester is a positive sign, ')
    print ('but not a guarantee that the code is correct.')
    
def main():
    testAll()

if __name__ == '__main__':
    main()
