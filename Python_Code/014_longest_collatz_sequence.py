#===============================================================================
# Problem 14: 
#
# The following iterative sequence is defined for the set of positive integers:
# 
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
# that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
#===============================================================================

# Author: Minqiang Li (any comments welcome at myfirstname.mylastname@gmail.com!
# https://github.com/minqiang/ProjectEuler

#===============================================================================
# I used a dictionary (lens) to keep track of the lengths. The program is 
# straightforward, but any comments to improve it is welcome! In particular, I 
# would like the program to run much faster!
#===============================================================================

from math import log

limit  = 1000001
lens = {i:0 for i in range(1, limit)}
for i in range( long(log(limit,2))+1 ):
    lens[2**i] = i+1
    
maxi, maxlen = 0, 0
    
for i in range(1, limit):
    if lens[i] <= 0:
        ilist = [i]
        newint = i
        while True:
            if newint%2 == 0:
                newint = newint/2
            else:
                newint = 3*newint+1
            ilist.insert(0,newint)
            
            if lens.has_key(newint) == False:
                lens[newint] = 0
    
            if lens[newint]>0:
                for j in range(1, len(ilist)):
                    lens[ilist[j]] = j+lens[newint]
                break
            
    if lens[i] > maxlen:
        maxi, maxlen = i, lens[i]
        
print(maxi, maxlen)
    
#===============================================================================
# Result:
# from timeit import timeit
# timeit(lambda: execfile("014_longest_collatz_sequence.py"), number=1)
# (837799, 525)
# 5.1999879917354175
#===============================================================================

    
    
