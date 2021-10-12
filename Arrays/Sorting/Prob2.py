'''Given an array of integers A, sort the array into a wave like array and return it, In other words, arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5.....
NOTE : If there are multiple answers possible, return the one that's lexicographically smallest.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        n = len(A)
        A.sort()
        for i in range(0, n-1, 2):
            A[i], A[i+1] = A[i+1], A[i]
        return A