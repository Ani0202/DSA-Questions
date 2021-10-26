'''Given an integer A, count and return the number of trailing zeroes.'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        A = A-1
        ans = 0
        while A & 1:
            ans += 1
            A = A>>1
            
        return ans
