'''Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1.'''

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A = int(A)
        if A == 0 or A == 1:
            return 0
            
        if A & (A-1) == 0:
            return 1
        else:
            return 0