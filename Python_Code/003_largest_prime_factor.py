#===============================================================================
# Problem 3:
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
#===============================================================================


# Author: Minqiang Li (any comments welcome at myfirstname.mylastname@gmail.com!


#===============================================================================
# The code below uses brute-force checking. Code is neither super-efficient,
# nor robust.  
# Once I found a prime factor, I eliminate this factor from the given integer.
# Any comments welcome!
#===============================================================================

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
 
given_number = 600851475143
i =2
lpf = -1 
while i<=given_number:
    if is_prime(i) & given_number%i == 0:
        lpf = i
        while given_number%i == 0: # eliminates this factor i
            given_number /= i
    i += 1
 
print(lpf)

