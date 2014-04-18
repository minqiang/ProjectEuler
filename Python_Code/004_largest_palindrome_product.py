#===============================================================================
# Problem 4:
# 
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
#===============================================================================


# Author: Minqiang Li (any comments welcome at myfirstname.mylastname@gmail.com!
# https://github.com/minqiang/ProjectEuler

#===============================================================================
# The program uses brute-force looping using two indices i, j where i<j.
# Early termination is checked to gain some efficiency.
#
# The program also solves a more general problem by allowing an input digits, 
# which is the number of digits in the two factors. For example,
# changing digits to 7 gives the result:
#        [99956644665999L, 9997647, 9998017]
#
#===============================================================================



def palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palin(digits):

    min0 = 10**(digits-1) -1
    max0 = 10**(digits) -1
    
    i = max0
    maxp = 0
    imin = min0
    
    while i>imin:
        j = max0;
        while j>i:
            p = i*j
            if palindrome(p):
                if p>maxp:
                    maxp = p
                    imin = maxp/max0
                    ivalue = i
                    jvalue = j
                break
            j -= 1
        i -= 1
        
    return [maxp, ivalue, jvalue]

given_digits = 3
print(largest_palin(given_digits))
            