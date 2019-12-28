#!/usr/bin/env python3
# 19fa103; john k johnstone; jkj at uab dot edu; mit license

import string
from remove_punctuation import *                # a helper function, to help you

# In Class Excerises
"""
Algorithm forvocabDictand a hint for testing:
- Read the file into one long string
- Split the string into words (in a list)
- For each word, translate to lowercase and remove punctuation
- Iterate through the list of words, building a dictionary
- With key = wrd, value = number of occurrences of that word
"""
#Counting Questions
"""
vocabSize Questions:
–how many unique words in Shakespeare’s 18th sonnet?
83
–how many unique words in “A Midsummer’s Night Dream”?
3040
–how many unique words in “Romeo and Juliet”?
3815

mostPopular Questions:
–what is the most popular word in Shakespeare’s 18th sonnet?
and
–what is the most popular word in “A Midsummer’s Night Dream”?
the
–what is the most popular word in “Romeo and Juliet”?
and

"""

def vocabDict (fn):

    """Vocabulary of a text.

    Collapse similar words into the same word before counting:
    'cat', 'Cat', 'cat!' are considered equivalent, representing the word 'cat'.

    Params: fn (string) filename of a file containing natural language text
    Returns: (dict) dictionary of unique words, collapsing Cat/cat/cat!
                   key = string w, value = int (#times w occurs in some version)
    """
    f = open(fn, "r", encoding="utf-8")
    s=f.read()
    f.close()
    ssplit = s.split()
    d={}
    
    for i in range(len(ssplit)):
        ssplit[i] = ssplit[i].lower()
        ssplit[i] = removePunctuation(ssplit[i])
        if ssplit[i] in d.keys():
            d[ssplit[i]] += 1
        else:
            d[ssplit[i]] = 1
            
    return d

print("#vocabDict Test Calls:")
print(vocabDict("sonnet_18_shakespeare.txt"))

def vocabSize (fn):

    """Size of vocabulary of a text.

    Params: fn (string) filename of some natural language text
    Returns: (int) number of unique words, collapsing Cat/cat/cat!
    """

    return len(vocabDict(fn))
    
##    f = open(fn, "r", encoding="utf-8")
##    s=f.read()
##    f.close()
##    ssplit = s.split()
##    d={}
##    uniqueWords = 0
##    
##    for i in range(len(ssplit)):
##        ssplit[i] = ssplit[i].lower()
##        removePunctuation(ssplit[i])
##        if ssplit[i] in d.keys():
##            d[ssplit[i]] += 1
##        else:
##            d[ssplit[i]] = 1
##    
##    for values in d.values():
##        if values == 1:
##            uniqueWords += 1
##        else:
##            uniqueWords = uniqueWords
##            
##    return  uniqueWords

print()
print("#vocabSize Test Calls:")
print(vocabSize("sonnet_18_shakespeare.txt"))
print(vocabSize("a_midsummer_nights_dream_folger.txt"))
print(vocabSize("romeo_and_juliet_folger.txt"))

def mostPopular (fn):

    """Find the most popular word in a text.

    Params: 
        fn (string) filename of some natural language text 
    Returns: (string/int 2-tuple) most popular word and its count
    """
    f = open(fn, "r", encoding="utf-8")
    s=f.read()
    f.close()
    ssplit = s.split()
    d={}
    popularWord = "the" #need to figure out how to grab first key

    for i in range(len(ssplit)):
        ssplit[i] = ssplit[i].lower()
        removePunctuation(ssplit[i])
        if ssplit[i] in d.keys():
            d[ssplit[i]] += 1
        else:
            d[ssplit[i]] = 1

    for w in d:
        if d[w] > d.get(popularWord):
            popularWord = w
        else:
            popularWord = popularWord

    return (popularWord, d[popularWord])

print()
print("#mostPopular Test Calls:")
print(mostPopular("sonnet_18_shakespeare.txt"))
print(mostPopular("a_midsummer_nights_dream_folger.txt"))
print(mostPopular("romeo_and_juliet_folger.txt"))

def nMostPopular (fn, n):

    """Find the n most popular words in a text.

    Params: 
        fn (string) filename of some natural language text 
        n (int) number of most popular words to return
    Returns: (list of 2-tuples) n most popular words 
              each is a 2-tuple: (ith most popular word, count)
    """
    pass

#Challenge:
"""
Remove stop words from the dictionary when counting.
del d[‘a’]
del d[‘the’]
del d[‘and’]
del d[‘or’]
"""
