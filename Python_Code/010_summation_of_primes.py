#===============================================================================
# Problem 10: 
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
#===============================================================================

# Author: Minqiang Li (any comments welcome at myfirstname.mylastname@gmail.com!
# https://github.com/minqiang/ProjectEuler

#===============================================================================
# This problem is related to Problem 7. 
# In fact, code change is extremely minimal.
# Any idea of speeding up code is welcome.
#===============================================================================


from math import sqrt

# given number num, check whether divisible by any number in plist
def not_divisible(num, plist):
    m = long(sqrt(num))
    for j in plist:
        if j>m:
            return True
        if num%j == 0:
            return False
    return True

plist = [2,3]
sum_prime = 5
i = plist[-1]

limit = 2000000
while i < limit:
    i += 2
    if not_divisible(i, plist):
        plist.append(i)
        sum_prime += i

print(sum_prime)
        