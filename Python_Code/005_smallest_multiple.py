#===============================================================================
# Problem 5:
# 
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all 
# of the numbers from 1 to 20?
#
#===============================================================================


# Author: Minqiang Li (any comments welcome at myfirstname.mylastname@gmail.com!
# https://github.com/minqiang/ProjectEuler

from math import sqrt
 
def is_prime(num):
    if num==2:
        return True
    elif num==1:
        return False
    for j in range(2, long(sqrt(num)+1)):
        if (num % j) == 0:
            return False
    return True

i = 2
limit = 20
number = 1

while i<= limit:
    if is_prime(i):
        p = i
        while p*i < limit:
            p *= i
        number *= p
    i += 1

print(number)
    
        