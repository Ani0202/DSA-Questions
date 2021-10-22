'''Given a matrix of integers A of size N x M in which each row is sorted.

Find an return the overall median of the matrix A.

Note: No extra memory is allowed.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.'''

from bisect import bisect_right

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        N = len(A)
        M = len(A[0])
        low = A[0][0]
        high = 0
        for i in range(N):
            high = max(high, A[i][M-1])
            low = min(low, A[i][0])
            
        m = (N*M + 1)//2
        
        while low <= high:
            mid = (low + high)//2
            n = [0]
            for i in range(N):
                n[0] += bisect_right(A[i], mid)
            if n[0] < m:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
