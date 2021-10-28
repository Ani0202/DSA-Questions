'''Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.'''

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        a = 0
        for i in range(a, len(A)):
            if A[i] == 0:
                A[a], A[i] = A[i], A[a]
                a += 1
                
        for i in range(a, len(A)):
            if A[i] == 1:
                A[a], A[i] = A[i], A[a]
                a += 1
                
        for i in range(a, len(A)):
            if A[i] == 2:
                A[a], A[i] = A[i], A[a]
                a += 1
        return A