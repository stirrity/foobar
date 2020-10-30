"""
The Grandest Staircase Of Them All
==================================

With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

Test cases
==========
Input:
Solution.solution(3)
Output:
    1

Input:
Solution.solution(200)
Output:
    487067745
"""


def solution(n):
    """
    This can be solved by dp
    dp[i][j] records the total number of combinations given i bricks with the highest one no larger than j bricks
    
    base cases:
      dp[0][0] == 1
      n < 3, no valid answer
    
    rule:
      dp[i][j] = dp[i][j-1] (all possibilities with a lower highest step) 
              + dp[i - j][min(j - 1, i - j)] (possibilities with highest step of j bricks, then i - j bricks remain and the highest step can be at most j - 1 or i - j bricks)
    
    return dp[n][n - 1], i.e. given n bricks with the highestest step no more than n - 1 bricks (securing 2 steps)
    
    example when n == 3:          
    0   1 0 0 0 
    1   0 1 0 0
    2   0 0 1 0 
    3   0 0 1 2
    return 1
    """
    if n < 3:
        return 0
    
    dp = [[0] * (n + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - j][min(j - 1, i - j)] + dp[i][j - 1]
    return dp[-1][-2]
