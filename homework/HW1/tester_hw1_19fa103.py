# CS103 Fall 2019 Johnstone
# HW1 tester: please do not change
# python3; copyright 2019 john k johnstone jkj at uab dot edu ; mit license

# check for syntax errors in the submission
print ("Checking for syntax errors ...", end='')
try:
    import hw1_19fa103                                  # the student's homework
except Exception as e:
    print ()
    print ('Your code contains a syntax error. Please correct and resubmit.')
    print (e)
    exit (1)
print ('passed')

########################################################################
### enforce HW1 constraints on syntax and style, for each fn
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

banned_tokens_hw1 = (
    'print,numpy,hypot,binom,' + 
    'and,or,not,if,for,while,str,string,in,is,len,list,range,' +
    'break,class,continue,dict,eval,except,filter,finally,global,hex,' +
    '__import__,lambda,map,open,set,slice,try,tuple,raise,' + 
    'repr,with,yield,[,],{,}')
banned_tokens = banned_tokens_hw1.split(',')
print ("Checking for violations of CS103 HW1 syntax constraints...", end='')
lint_103 (inspect.getsource (hw1_19fa103), banned_tokens)
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
def grade (test_id, answer, correct_answer, nCorrect):
    """Grade an answer.
    Params:
        test_number (str): ID of the test
        answer (flexible type): submitted answer
        correct_answer (same type as answer): correct answer
        nCorrect (int): # correct so far
    Returns: (int) # correct so far after considering this latest answer
    """
    
    if answer != None:
        print (test_id + ' should be ' + str(correct_answer), end='')
        print ('. Your answer: '+str(answer), end='  ')
    typeCorrect = type(answer) == type(correct_answer)
    if answer != None and typeCorrect and answer == correct_answer:
        nCorrect = nCorrect + 1
        print ('CORRECT')
    else:
        print ('WRONG')
    return nCorrect

def gradeApprox (test_id, answer, correct_answer, nCorrect):
    """Grade an answer.
    Params:
        test_number (str): ID of the test
        answer (float): submitted answer
        correct_answer (float): correct answer
        nCorrect (int): # correct so far
    Returns: (int) # correct so far after considering this latest answer
    """
    
    if answer != None:
        print (test_id + ' should be about ', end='')
        print (str (significant (correct_answer, 7)), end='')
        print ('. Your answer: ', end='')
        print (str (significant (answer, 7)), end='  ')
    if answer != None and approxEq (answer, correct_answer):
        nCorrect = nCorrect + 1
        print ('CORRECT')
    else:
        print ('WRONG')
    return nCorrect

################################################################################
################################################################################
################################################################################
from hw1_19fa103 import * 
# allows shorthand (`areaCircle` rather than `hw1_19fa103.areaCircle`)

def testF (correct):
    print ('Testing f.')
    correct = gradeApprox ('t1', f (0.),  -3., correct)
    correct = gradeApprox ('t2', f (1.),   2., correct)
    correct = gradeApprox ('t3', f (-1.), -8., correct)
    print ()
    return correct

def testAreaCircle (correct):
    print ('Testing areaCircle.')
    correct = gradeApprox ('t4', areaCircle (1.), 3.141592653589793, correct)
    correct = gradeApprox ('t5', areaCircle (.1), 0.031415926535897934, correct)
    correct = gradeApprox ('t6', areaCircle (12.34), 478.3879062809779, correct)
    print ()
    return correct
    
def testNSnookerBall (correct):
    print ("Testing nSnookerBall.")
    correct = grade ('t7', nSnookerBall (5), 15, correct)
    correct = grade ('t8', nSnookerBall (0), 0, correct)
    correct = grade ('t9', nSnookerBall (3), 6, correct)
    correct = grade ('t10', nSnookerBall (20), 210, correct)
    print()
    return correct

def testEApproximately (correct):
    print ("Testing eApproximately.")
    correct = gradeApprox ('t11', eApproximately (1), 2., correct)
    correct = gradeApprox ('t12', eApproximately (2), 2.25, correct)
    correct = gradeApprox ('t13', eApproximately(10),2.5937424601000023,correct)
    correct = gradeApprox('t14',eApproximately (100),2.7048138294215285,correct)
    print()
    return correct

def testVolCone (correct):
    print ("Testing volCone.")
    correct = gradeApprox ('t15', volCone (1., 1.), 1.0471975511965976, correct)
    correct = gradeApprox ('t16', volCone (2., 2.), 8.377580409572781, correct)
    correct = gradeApprox ('t17', volCone (3., 2.), 18.84955592153876, correct)
    print ()
    return correct

def testDistOrigin (correct):
    print ('Testing distOrigin().')
    correct = gradeApprox ('t18', distOrigin (0., 0.), 0., correct)
    correct = gradeApprox ('t19', distOrigin (3., 4.), 5., correct)
    correct = gradeApprox ('t20', distOrigin (0., 2.), 2., correct)
    correct = gradeApprox ('t21', distOrigin (1., 1.), 2**.5, correct)
    print ()
    return correct

def testLengthSegment (correct):
    print ('Testing lengthSegment().')
    result  = lengthSegment (200,200,200,203,204,200) 
    correct = gradeApprox ('t22', result, 5, correct)
    result  = lengthSegment (100, 0, 100, 101, 0, 101)
    correct = gradeApprox ('t23', result, 2**.5, correct)
    print ('Passed.  (Add more tests to gain extra confidence.)')
    print()
    return correct
    
########################################
# HW1 main
########################################

def testAll():
    correct = 0
    print ('Hello, ' + myName() + '. (If this is not your name, fix myName.)')
    print ('Commencing unit tests...')
    correct = testF (correct)
    correct = testAreaCircle (correct)
    correct = testNSnookerBall (correct)
    correct = testEApproximately (correct)
    correct = testVolCone (correct)
    correct = testDistOrigin (correct)
    correct = testLengthSegment (correct)
    print ('Testing results: ' + str(correct) + ' out of 23')

def main():
    testAll()

if __name__ == '__main__':
    main()
