'''You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        start = -1
        end = -1
        B = sorted(A)
        for i in range(n):
            if A[i] != B[i]:
                start = i
                break
        if start == -1:
            return [-1]
            
        for i in range(n-1, -1, -1):
            if A[i] != B[i]:
                return [start, i]