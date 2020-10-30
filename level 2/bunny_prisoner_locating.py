"""
Bunny Prisoner Locating
=======================

Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

| 7
| 4 8
| 2 5 9
| 1 3 6 10

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 

For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners). 

Write a function solution(x, y) which returns the prisoner ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your solution as a string representation of the number.


Test cases
==========
Input:
solution.solution(5, 10)
Output:
    96

Input:
solution.solution(3, 2)
Output:
    9
"""

def solution(x, y):
    """
    First find which layer (x, y) is on, numbers are distributed 1, 2, 3, ... based on layers
    origin (1, 1) sum to 2
    point (x, y) sum to x + y is located in x + y - 1 layer, with x + y - 1 numbers in the layer
    """  
    layer = x + y - 1
    
    # before cur-layer, there are pre_sum numbers
    pre_sum = (layer - 1) * layer // 2
    
    # x means the idx of the res in cur_layer
    res = pre_sum + x
    return str(res)
    
## In java, the res number, no larger than 500,000,000, is actually within the range of Integer. So no need to write a specific function to do string caculation.
