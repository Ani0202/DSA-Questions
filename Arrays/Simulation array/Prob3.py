'''Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.



Input Format:

The first and the only argument contains an integer, A.
Output Format:

Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:

1 <= A <= 1000'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        left = 0
        right = A-1
        top = 0
        bottom = A-1
        direction = 0
        j = 1
        mat = [[0 for _ in range(A)] for _ in range(A)]
        while left <= right and top <= bottom:
            if direction == 0:
                for i in range(left, right + 1):
                    mat[top][i] = j
                    j = j + 1
                top = top + 1
                    
            elif direction == 1:
                for i in range(top, bottom + 1):
                    mat[i][right] = j
                    j = j + 1
                right = right - 1
                    
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    mat[bottom][i] = j
                    j = j + 1
                bottom = bottom - 1
                    
            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    mat[i][left] = j
                    j = j + 1
                left = left + 1
                
            direction = (direction + 1)%4
            
        return mat
                