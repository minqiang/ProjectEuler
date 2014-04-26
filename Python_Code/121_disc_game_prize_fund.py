#===============================================================================
# Problem 121:
#
# A bag contains one red disc and one blue disc. In a game of chance a player 
# takes a disc at random and its colour is noted. After each turn the disc is 
# returned to the bag, an extra red disc is added, and another disc is taken 
# at random.
#
# The player pays $1 to play and wins if they have taken more blue discs than 
# red discs at the end of the game.
#
# If the game is played for four turns, the probability of a player winning 
# is exactly 11/120, and so the maximum prize fund the banker should allocate 
# for winning in this game would be $10 before they would expect to incur 
# a loss. Note that any payout will be a whole number of pounds and also 
# includes the original $1 paid to play the game, so in the example given the 
# player actually wins $9.
#
# Find the maximum prize fund that should be allocated to a single game in 
# which fifteen turns are played.
#
#===============================================================================

# Author: Minqiang Li (any comments welcome at myfirstname.mylastname@gmail.com!
# https://github.com/minqiang/ProjectEuler

#===============================================================================
# At each turn T, we let (T, k) to denote a node with k blue discs. It is easy
# to see that the nodes will give us a binary recombining tree. Given the 
# probabilities of reaching the nodes at turn T, we can work out the 
# probabilities of reaching the nodes at turn T+1. We can then find out the 
# winning probability (denote as P) at the end of all the turns. The funders 
# need to at least break even:
#         P*(1-prize) + (1-P)*1 > 0
# or equivalently:
#         prize < 1/P
# Maximum integer prize is then floor(1/P).
#===============================================================================

from math import factorial

total_turns = 15
# end of turn 1 outcome probabilities (two outcomes). recorded only numerators.
# The denominator is always T!
p = [1,1] 

for T in range(2,total_turns+1):
    p = [ T*p[i-1] + p[i] for i in range(1, len(p)) ]
    p.insert(0,1)
    p.append(factorial(T))

prize = factorial(T+1)/ sum(p[:T/2+1]) 
print(prize)

#===============================================================================
# Result:
# from timeit import timeit
# timeit(lambda: execfile("121_disc_game_prize_fund.py"), number=1)
# 2269
# 0.0008206724988752967
#===============================================================================