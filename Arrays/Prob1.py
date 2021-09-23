'''Given an integer array A of size N.

You can pick B elements from either left or right end of the array A to get maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        curr_sum = sum(A[:B])
        curr_max = curr_sum
        for i in range(B):
            curr_sum = curr_sum - A[B -i - 1] + A[-(i + 1)]
            curr_max = max(curr_sum, curr_max)
        return curr_max