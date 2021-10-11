'''You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.'''

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]

        for i in range(n):
            for j in range(n//2):
                A[i][j], A[i][-j-1] = A[i][-j-1], A[i][j]

        return A