#===============================================================================
# Problem 9
# 
# A Pythagorean triplet is a set of three natural numbers, 
# a < b < c, for which,
#               a^2 + b^2 = c^2
# For example, 3^2 + 4^2 =  5^2.
# 
# There exists exactly one Pythagorean triplet 
# for which a + b + c = 1000.
# Find the product abc.
#===============================================================================


# Author: Minqiang Li (any comments welcome at myfirstname.mylastname@gmail.com!
# https://github.com/minqiang/ProjectEuler

#===============================================================================
# General solutions are given by multiples of
# a = 2mn
# b = m^2 - n^2
# c = m^2 + n^2
# where m,n are coprime, and m-n is odd.
# Therefore, 
# a + b +c = k(2mn+ 2m^2) 
# i.e.
# 2 k m (m+n)= 1000 = 2^3 * 5^3
# Since (m+n) = (m-n) + 2n also must be odd,
# we have several cases for m+n: 1, 5, 25, 125.
# The code then loops over n.
#===============================================================================


from math import sqrt
nmax = long(sqrt(1000/2)) # c > 2*n^2, but c < 1000

mplusn = [1,5,25,125]

for n in range(1, nmax):
    mlist = [x - n for x in mplusn if (x-2*n)%2 ==1 and x >= 2*n and 500% (x-n)*x ==0]
    if mlist:
        m = mlist[0] # the problem told us solution is unique. so early termination
        k = 500/(m+n)/m
        a = 2*m*n
        b = m**2 - n**2
        c = m**2 + n**2
        break

result = k**3*a*b*c
print(result)

       
    
    