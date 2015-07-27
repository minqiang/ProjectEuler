#===============================================================================
# Problem 7:
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
#
# What is the 10001st prime number?
#===============================================================================

# Author: Minqiang Li (any comments welcome at myfirstname.mylastname@gmail.com!
# https://github.com/minqiang/ProjectEuler

#===============================================================================
# Simple method by checking numbers one by one using the function is_divisible. 
# The primes are saved in the list plist to speed up computation.
#===============================================================================

from math import sqrt

# given number num, check whether divisible by any number in plist
def not_divisible(num, plist):
    m = long(sqrt(num))+1
    for j in plist:
        if j>m:
            return True
        if num%j == 0:
            return False
    return True

plist = [2,3]
num_prime = 2
i = plist[-1]

limit = 10001
while num_prime < limit:
    i += 2
    if not_divisible(i, plist):
        plist.append(i)
        num_prime += 1

print(plist[-1])
        
        
        

    