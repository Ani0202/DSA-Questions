'''Write a function that takes an integer and returns the number of 1 bits it has.'''

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        ans = 0
        while A > 0:
            A = A & A-1
            ans += 1
            
        return ans

