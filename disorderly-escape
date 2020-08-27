"""
Write a function solution(w, h, s) that takes 3 integers and returns the number of unique, non-equivalent configurations that can be found on a star grid w blocks wide and h blocks tall where each celestial body has s possible states. Equivalency is defined as above: any two star grids with each celestial body in the same state where the actual order of the rows and columns do not matter (and can thus be freely swapped around). Star grid standardization means that the width and height of the grid will always be between 1 and 12, inclusive. And while there are a variety of celestial bodies in each grid, the number of states of those bodies is between 2 and 20, inclusive. The solution can be over 20 digits long, so return it as a decimal string.  The intermediate values can also be large, so you will likely need to use at least 64-bit integers.

For example, consider w=2, h=2, s=2. We have a 2x2 grid where each celestial body is either in state 0 (for instance, silent) or state 1 (for instance, noisy).  We can examine which grids are equivalent by swapping rows and columns.

00
00

In the above configuration, all celestial bodies are "silent" - that is, they have a state of 0 - so any swap of row or column would keep it in the same state.

00 00 01 10
01 10 00 00

1 celestial body is emitting noise - that is, has a state of 1 - so swapping rows and columns can put it in any of the 4 positions.  All four of the above configurations are equivalent.

00 11
11 00

2 celestial bodies are emitting noise side-by-side.  Swapping columns leaves them unchanged, and swapping rows simply moves them between the top and bottom.  In both, the *groupings* are the same: one row with two bodies in state 0, one row with two bodies in state 1, and two columns with one of each state.

01 10
01 10

2 noisy celestial bodies adjacent vertically. This is symmetric to the side-by-side case, but it is different because there's no way to transpose the grid.

01 10
10 01

2 noisy celestial bodies diagonally.  Both have 2 rows and 2 columns that have one of each state, so they are equivalent to each other.

01 10 11 11
11 11 01 10

3 noisy celestial bodies, similar to the case where only one of four is noisy.

11
11

4 noisy celestial bodies.

There are 7 distinct, non-equivalent grids in total, so solution(2, 2, 2) would return 7.


-- Test case --
Input:
solution.solution(2, 3, 4)
Output:
    430
"""


def solution(w, h, s):
    # Your code here
    
    def factorial(n):
        """
        calculate n!, ie 1 * 2 * .. * n
        """
        if n < 2:
            return 1
        res = 1
        for i in range(2, n + 1):
            res *= i
        return res
    
    def gcd(a, b):
        """
        get the greatest common divisor
        """
        if b == 0:
            return -1
        mod = a % b
        if mod == 0:
            return b
        return gcd(b, mod)
        
    def counter(cycle_lens):
        """
        get a dictionary of different cycle lengths and their counts in the combination
        """
        first, cur, n = 0, 0, len(cycle_lens)
        cycle_lens_count = {}
        while cur < n:
            while cur < n and cycle_lens[cur] == cycle_lens[first]:
                cur += 1
            cycle_lens_count[cycle_lens[first]] = cur - first
            first = cur
        return cycle_lens_count
    
    def cycle_count(cycle_lens_count, n):
        """
        get the total possible cycles in one dimension given a cycle conbination
        """
        # total permutations in this dimension
        total_counts = factorial(n) 
        for length, count in counter(cycle_lens_count).items():
            # length**count as for each cycle, not permutation needed within the circle
            # factorial(b) as for no permutation of cycles with the same length needed
            total_counts //= (length**count) * factorial(count)
        return total_counts    
    
    def cycle_partitions(n, start = 1):
        """
        generage the partition of the cycle with total length of n
        the cycle lengths in each partition is ascending
        """
        yield [n]
        for i in range(start, n // 2 + 1):
            for partition in cycle_partitions(n - i, i):
                yield [i] + partition
                
    total_cycles = 0
    for cp_w in cycle_partitions(w):
        for cp_h in cycle_partitions(h):
            # group is sopposed to be 1 / |An|, but to avoid loss of accuracy, so use group = 1/|An|* fac(h) * fac(w) which is a integer/long
            group = cycle_count(cp_w, w) * cycle_count(cp_h, h)
            # for each sub-cycle A in cp_h, when combined with a new sub-cycle B cp_w, the number of new cycles is gcd(len(A), len(B))
            num_cycles = sum([sum([gcd(sub_w, sub_h) for sub_w in cp_w]) for sub_h in cp_h])
            # Polya equation
            total_cycles += group * (s**num_cycles)
    return str(total_cycles // (factorial(w) * factorial(h)))
