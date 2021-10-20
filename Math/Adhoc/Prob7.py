'''Given a target A on an infinite number line, i.e. -infinity to +infinity.
You are currently at position 0 and you need to reach the target by moving according to the below rule:

In ith move you can take i steps forward or backward.
Find the minimum number of moves required to reach the target.'''

import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        A = abs(A)
        n = math.ceil((-1.0 + math.sqrt(1 + 8.0 * A)) / 2)
        sm = n * (n+1) / 2
        d = sm - A
        if d%2 == 0:
            return n
        elif (d+n+1) % 2 == 0:
            return n+1
        else:
            return n+2
