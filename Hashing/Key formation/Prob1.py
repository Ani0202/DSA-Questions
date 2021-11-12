'''
Given an 1D integer array A containing N distinct integers.

Find the number of unique pairs of integers in the array whose XOR is equal to B.

NOTE:

Pair (a, b) and (b, a) is considered to be same and should be counted once.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        hMap = dict()
        n = len(A)
        for i in range(n):
            if B^A[i] in hMap:
                ans += 1
            hMap[A[i]] = i
            
        return ans
