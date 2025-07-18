# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 2018

@author: clham
"""

a=1
b=1

length = int(input('How many Fibonacci Numbers do you want?  '))

L = range(length)

for x in L:
    if x == 0:
        L[x] = a
    else:
        L[x] = b
        temp = b
        b = a + b
        a = temp

print(L)
