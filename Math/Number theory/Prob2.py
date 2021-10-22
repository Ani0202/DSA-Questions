'''Given an integer A, return the number of trailing zeroes in A!.

Note: Your solution should be in logarithmic time complexity.'''

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        i = 1
        ans = 0
        while int(A/(5**i)) > 0:
            ans += int(A/5**i)
            i += 1
            
        return ans
