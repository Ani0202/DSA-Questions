'''Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.'''

import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A == 1:
            return 1
        for i in range(1, int(A**0.5 + 1)):
            for j in range(2, int(math.log2(A) + 1)):
                if A == i**j:
                    return 1
                    
        return 0
                
        