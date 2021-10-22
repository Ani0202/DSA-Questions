'''Given a matrix of integers A of size N x M and an integer B.

Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.'''

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        N = len(A)
        M = len(A[0])
        low = 0
        high = N*M - 1
        while low <= high:
            mid = (low + high) // 2
            i = int(mid / M)
            j = int(mid % M)
            if A[i][j] == B:
                return 1
            elif A[i][j] < B:
                low = mid + 1
            else:
                high = mid - 1
                
        return 0
