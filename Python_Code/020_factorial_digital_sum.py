#===============================================================================
# Problem 020: 
# 10! = 3628800, and the sum of the digits in the number 
# 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#===============================================================================


# Author: Minqiang Li
## https://github.com/minqiang/ProjectEuler


from math import factorial
num = factorial(100)
charlist = list(str(num))
numlist = [int(x) for x in charlist]
print(sum(numlist))

#===============================================================================
# Result:
# 648
#===============================================================================