"""
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly. 

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Test cases
==========
Input:
solution.solution('15')
Output:
    5

Input:
solution.solution('4')
Output:
    2
"""

def solution(input):
    """
    BFS algorithm to search through the entire possibilities of meta numbers. 
    Set is needed to reduce unnecessary calculation.
    String type is keeped to be compatible with Set. List is not suitable here. 
    """
    
    # Dictionaries to make string operations easier, it does not require a lot of conversion between string and int types 
    divide_dict_single = {'9': '4', '8': '4', '7': '3', '6': '3', '5': '2', '4': '2', '3': '1', '2': '1', '1': '0', '0': '0'}
    divide_dict_with_remain = {'9': '9', '8': '9', '7': '8', '6': '8', '5': '7', '4': '7', '3': '6', '2': '6', '1': '5', '0': '5'}
    odds = ['1', '3', '5', '7', '9']
    
    def minus_one(s):
      """
      Minus 1 from the string s
      """
        if s == '0':
            return '1-'
        l = list(s) 
        for i in range(len(l)):
            if l[i] == '0':
                l[i] = '9'
            else:
                l[i] = str(int(l[i]) - 1)
                break
        if l[-1] == '0':
            l.pop()
        return ''.join(l)
        
    def plus_one(s):
      """
      Plus one to the string s
      """
        l = list(s)
        for i in range(len(l)):
            if l[i] == '9':
                l[i] = '0'
            else:
                l[i] = str(int(l[i]) + 1)
                break
        if l[-1] == '0':
            l.append('1')
        return ''.join(l)
    
    def divide_by_two(s):
      """
      Divide the string s by 2. Prechecked before the calling of this function
      """
        remain = 0
        l = list(s)
        for i in range(len(l)-1, -1, -1):       
            new_remain = 1 if l[i] in odds else 0    
            l[i] = divide_dict_with_remain[l[i]] if remain else divide_dict_single[l[i]]
            remain = new_remain
        if l[-1] == '0':
            l.pop()
        return ''.join(l)    

    if input == '1':
        return 0
        
    import Queue
    q = Queue.Queue()
    # if the number is negative, two more steps are needed after reach '-1'
    to_add = 0
    if input[0] == '-':
        input = input[1:]
        to_add = 2      
    
    # string is reversed, so the list pop() is easier when the leading number is '0'
    s = input[::-1]
    step = 0
    checked = set()
    q.put_nowait(s)       
    checked.add(s)
    while q:
        step += 1
        size = q.qsize()
        for i in range(size):
            cur_str = q.get_nowait()
            # if odd, then +1 or -1            
            if cur_str[0] in odds:               
                str_minus = minus_one(cur_str)
                if str_minus == '1':
                    return step + to_add
                if str_minus not in checked:
                    checked.add(str_minus)
                    q.put_nowait(str_minus)
        
                str_plus = plus_one(cur_str)
                if str_plus not in checked:
                    checked.add(str_plus)
                    q.put_nowait(str_plus)
            # if even, divide by 2.
            else:
                str_divide = divide_by_two(cur_str)
                if str_divide == '1':
                    return step + to_add
                if str_divide not in checked:
                    checked.add(str_divide)
                    q.put_nowait(str_divide)
    # Not really needed, but can be used to marked malfunction
    return -1
