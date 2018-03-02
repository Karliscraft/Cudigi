#!/usr/bin/env python2
from __future__ import print_function
import random
if 5/2==1.5:
    input=lambda *args, **kwargs: raw_input(*args,**kwargs)
consonants=['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 
'Q', 'R', 'S', 'T', 'V', 'X', 'Z']
vowels=['A','E','I','O','U']
length=random.randint(int(input("Min length: ")), int(input("Max length: ")))
vowelflag=False
if random.randint(0,1)==1: vowelflag=True
wordt=[]
for i in range(1,length):
    if vowelflag:
        vowelflag=False
        wordt.append(vowels[random.randint(0,len(vowels)-1)].lower())
    else:
        vowelflag=True
        wordt.append(consonants[random.randint(0,len(vowels)-1)].lower())
capitalization=random.randint(0,1)
if capitalization:
    wordt[0]=wordt[0].upper()
    final="".join(wordt)
else:
    final="".join(wordt).upper()
print(final)
