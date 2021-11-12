'''Given a 2D integer matrix A of size N x N find a B x B submatrix where B<= N and B>= 1, such that sum of all the elements in submatrix 
is maximum.'''

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        sumArr = [[None] * n for i in range(n)]
        maxSum = -float('inf')
        for i in range(n):
            tempSum = sum(A[i][0:B])
            sumArr[i][0] = tempSum
            for j in range(1, n-B+1):
                tempSum += (A[i][j+B-1] - A[i][j-1])
                sumArr[i][j] = tempSum
                
        for j in range(n-B+1):
            tempSum = 0
            for i in range(B):
                tempSum += sumArr[i][j]
            maxSum = max(maxSum, tempSum)
            for i in range(1, n-B+1):
                tempSum += (sumArr[i+B-1][j] - sumArr[i-1][j])
                maxSum = max(maxSum, tempSum)
                
        return maxSum
            
            