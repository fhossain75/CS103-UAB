#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# 19fa103; john k johnstone; jkj at uab dot edu; mit license

import lab05_19fa103 as lab05 

print ('readAndPrint tests')
lab05.readAndPrint ('limerick.txt')
lab05.readAndPrint ('sonnet_18_shakespeare.txt')
print ()
print ('splitText tests')
print (lab05.splitText ('short.txt'))
print (lab05.splitText ('limerick.txt'))
print ()
print ('countWord tests')
print (lab05.countWord ('short.txt'))
print (lab05.countWord ('limerick.txt'))
print (lab05.countWord ('sonnet_18_shakespeare.txt'))
print (lab05.countWord ('le_petit_prince_utf8.txt'))
print ()
print ('lastChar tests')
print (lab05.lastChar ('short.txt'))
print (lab05.lastChar ('limerick.txt'))
s = lab05.lastChar ('sonnet_18_shakespeare.txt')
print (s)       
# write to the file 'sonnet_last.txt' (don't forget to close after writing)
s = lab05.lastChar ('canto1_commedia_dante_edited.txt')
print (s)
# write to the file 'canto_last.txt'
print ()
print ('lastWord tests')
print (lab05.lastWord ('short.txt'))
print (lab05.lastWord ('limerick.txt'))
print (lab05.lastWord ('sonnet_18_shakespeare.txt'))
print (lab05.lastWord ('le_petit_prince_utf8.txt'))

# upload the following files to Canvas:
# 'sonnet_last.txt'
# 'canto_last.txt'
