# 19fa103; john k johnstone; jkj at uab dot edu; mit license

# this is the structure of the test script for HW3;
# please **replace all these tests by your own**
# the tests presently in this script are the same tests from the tester:
# do not duplicate any of these;
# I encourage you to choose your test data creatively and wisely
# (but at least give me valid test data)

import hw3_19fa103 as hw3

print ('eCount tests')
print (hw3.eCount ('Every e please.'), 'should be', 5)
print (hw3.eCount ('everyone'), 'should be', 3)
print (hw3.eCount ('To be or not to be, that is the question.'), 'should be', 4)
print (hw3.eCount ('nothing at all'), 'should be', 0)
print (hw3.eCount ("Faisal is taking Computer Science 103."), 'should be', 3)
print (hw3.eCount ("My cat name is Burberry."), 'should be', 2)
print ()

print ('pigglyWiggly tests')
print (hw3.pigglyWiggly ('dog'), 'should be', 'ogday')
print (hw3.pigglyWiggly ('cat'), 'should be', 'atcay')
print (hw3.pigglyWiggly ('each'), 'should be', 'eachyay')
print (hw3.pigglyWiggly ('every'), 'should be', 'everyyay')
print (hw3.pigglyWiggly ('are'), 'should be', 'areyay')
print (hw3.pigglyWiggly ('burberry'), 'should be', 'urberrybay')
print ()

print ('argLongest tests')
print (hw3.argLongest (['bling', 'loving', 'hating', 'liking']), 'should be', 1)
print (hw3.argLongest (['jewelry', 'bling', 'necklace']), 'should be', -1)
print (hw3.argLongest (['walking','running','jogging','attempting']), 'should be', 3)
print (hw3.argLongest (['cat', 'dog', 'fish', 'rabit']), 'should be', 1)
print (hw3.argLongest (['learn', 'wishing', 'learning', 'walk', 'walking']), 'should be', 2)
print ()

print ('hurray tests')
print (hw3.hurray (5), 'should be',  '0hurrayhurray3hurray5')
print (hw3.hurray (10), 'should be', '0hurrayhurray3hurray567hurray910')
print (hw3.hurray (16), 'should be ', end='')
print ('0hurrayhurray3hurray567hurray9101112131415hurray')
print (hw3.hurray (3), 'should be',  '0hurrayhurray3')
print (hw3.hurray (9), 'should be', '0hurrayhurray3hurray567hurray9')
print ()

print ('eApprox tests')
print (hw3.eApprox (1), 'should be', 2.25)
print (hw3.eApprox (2), 'should be', 2.44140625)
print (hw3.eApprox (3), 'should be', 2.6328787177279187)
print (hw3.eApprox (4), 'should be', 2.823)
print (hw3.eApprox (5), 'should be', 3.014)
