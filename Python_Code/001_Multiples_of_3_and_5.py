# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

# Author: Minqiang Li
## https://github.com/minqiang/ProjectEuler

#===============================================================================
# Tested using larger limit and it shows that reduce is slightly
# faster than a for loop.
#===============================================================================

multiples = [x for x in range(1000) if (x%3==0 or x%5==0)]
result = reduce(lambda a,b: a+b, multiples)
print(result)