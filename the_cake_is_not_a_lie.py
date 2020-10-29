"""
The cake is not a lie!
======================

Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members of the Bunny Rebellion, and she beat her personal high score in Tetris. To celebrate, she's ordered cake for everyone - even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone, you'll get in big trouble. 

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("abcabcabcabc")
Output:
    4

Input:
solution.solution("abccbaabccba")
Output:
    2

-- Java cases --
Input:
Solution.solution("abcabcabcabc")
Output:
    4

Input:
Solution.solution("abccbaabccba")
Output:
    2
"""

def solution(s):
    # Your code here
    """
    First counts all letters in the str, find the greatest common divisor
    Decrease the divisor as long as it is still valid until 1
    Check if the divisor works, if yest return the divisor
    Reach 1 then return 1 
    """
    
    def gcd(one, two):
        """
        Find the greatest common divisor of two non-negative intergers
        """
        if one == 0:
            return two
        return gcd(two % one, one)
    
    def get_counts(s):
        """
        Get the non-repeated counts of different characters in the input string.
        """
        counts = {}
        for ch in s:
            if ch not in counts:
                counts[ch] = 0
            counts[ch] += 1
        return list(set([counts[ch] for ch in counts]))      
    
    def get_divisor(l):
        """
        Find the greatest divisor of a given non-negative integer list
        """
        if not l:
            return -1
        res = l[0]
        for num in l:
            res = gcd(res, num)
        return res
  
    def is_valid_divisor(l, divisor):
        """
        Check if a number is a valid common divisor of all the integer in a list
        """
        for num in l:
            if num % divisor != 0:
                return False
        return True
    
    def valid_subsequence(s, length):
        """
        Check if a input string has repeated substring of a given length 
        Only start of 0-index is needed, as the start point can be shifted to any position if there are repeated substrings.
        """
        cur = length
        while cur + length <= len(s):
            for i in range(length):
                if s[i] != s[cur + i]:
                    return False
            cur += length
        return True
  
    if not s:
        return 0    
    list_num = get_counts(s) 
    greatest_divisor = get_divisor(list_num)
    
    # Check the divisor from the greatest possible to 1
    while greatest_divisor > 1:
        if is_valid_divisor(list_num, greatest_divisor):
            length = len(s) // greatest_divisor
            if valid_subsequence(s, length):
                return greatest_divisor
        greatest_divisor -=1
    return 1
