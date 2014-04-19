#===============================================================================
# Problem 6:
#
# The sum of the squares of the first ten natural numbers is,
# 
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 2640.
# 
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.
#===============================================================================

# Author: Minqiang Li (any comments welcome at myfirstname.mylastname@gmail.com!
# https://github.com/minqiang/ProjectEuler

#===============================================================================
# The difference is given by the formula n(3n^3 + 2n^2 - 3n -2)/12.
#===============================================================================

n=100
print( n*(3*n**3 + 2*n**2 - 3*n -2)/12)