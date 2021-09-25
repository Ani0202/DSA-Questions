'''Find the contiguous subarray within an array, A of length N which has the largest sum.'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        ans = A[0]
        temp_sum = 0
        for i in range(n):
            temp_sum = temp_sum + A[i]
            if ans < temp_sum:
                ans = temp_sum
            if temp_sum<0:
                temp_sum = 0
            
        return ans