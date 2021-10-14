'''Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.'''

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        M = len(A)
        N = len(A[0])
        rows, cols = set(), set()
        for i in range(M):
            for j in range(N):
                if A[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        for i in range(M):
            for j in range(N):
                if (i in rows) or (j in cols):
                    A[i][j] = 0
                
        return A