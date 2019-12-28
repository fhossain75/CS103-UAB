################################################################################
# HW4 CS103 Fall 2019

# I declare that I have completed this assignment completely and entirely
# on my own, without any consultation with others.
# I have read the UAB Academic Honor Code and understand that any breach
# of the Honor Code may result in severe penalties.

# name: Faisal Hssain
# blazerid: faisal75
################################################################################

################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE 'Alan Turing' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Faisal Hossain'
################################################################################

##############
# HW4 PROBLEMS
##############

def replaceLeadingB9 (s):

    """Create a string of pure digits from a B00 number.

    >>> replaceLeadingB9 ('B01234567')
    001234567

    You should not use a for loop for this question.

    Params: s (str): a string of length 9, beginning with B
    Returns: (str) s with the first character (the B) replaced by a 0
    """
    return "0"+s[1:]

def replaceAllB (s):

    """Replace all B's by 0's in a string.

    >>> replaceAllB ('B01234567')
    001234567
    >>> replaceAllB ('5B6B7B8B9')
    506070809
    >>> replaceAllB ('BBBB')
    '0000'
    >>> replaceAllB ('bbbb')
    'bbbb'

    You should use a for loop for this question.
    
    Params: s (str): a string
    Returns: (str) s with each B replaced by 0
    """
    x = ""
    for i in range(len(s)):
        if s[i] == "B":
            x += "0"
        else:
            x += s[i]
    return x

def replaceAllInPrefix (s, c, d):

    """Replace all c's by 0's in the length d prefix of a string.

    Note that c is a variable name, not the character c.
    
    >>> replaceAllInPrefix ('B01234567', 'B', 9)
    001234567
    >>> replaceAllInPrefix ('donkey', 'd', 1)
    0onkey
    >>> replaceAllInPrefix ('agent 007', '7', 8)
    agent 007
    >>> replaceAllInPrefix ('agent 007', '7', 9)
    agent 000
    >>> replaceAllInPrefix ('anything', 'z', 0)
    'anything'

    You should use a for loop for this question.

    Params:
        s (str): a string
        c (str): a string of length 1 (i.e., a character)
        d (int): length of prefix of interest (d >= 0)
    Returns: (str): s with each c replaced by 0, 
                    unless the c occurs past the prefix of length d
    """
    x = ""
    for i in range(d):
        if s[i] == c:
            x += "0"
        else:
            x += s[i]
    y = len(s) - d +1
    
    return x + s[d:y]

def replaceAll (s, ch, d):

    """Given a string, a character, and a digit, 
       replace all of those characters in the string by that digit.

    >>> replaceAll ('B01234567', 'B', 0)
    001234567
    >>> replaceAll ('abracadabra', 'a', 1)
    1br1c1d1br1

    You should use a for loop for this question.
    
    Params:
        s (str): a string
        ch (str): a string of length 1 (i.e., a character)
        d (int): digit with which to replace c
    Returns: (str) s with each ch replaced by d
    """
    x = ""
    for i in range(len(s)):
        if s[i] == str(ch):
            x += str(d)
        else:
            x += s[i]
    return x

def pages (nDigit):

    """How many pages are in a book if n digits were used to print its pages?

    You may assume every page is numbered and the numbering starts at 1.
    For example, a book of 11 pages requires 13 digits
    (1,2,3,4,5,6,7,8,9,10,11) so `pages(13)` is 11.

    >>> pages (13)
    11
    >>> pages (201)
    103

    Params: nDigit (int): #digits used by printer to number the pages of a book
    Returns: (int) #pages in the book
    """
