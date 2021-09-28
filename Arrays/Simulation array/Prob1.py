'''Given an integer array A of size N.

You need to check that whether there exist a element which is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it.

If it exists return 1 else return 0.

NOTE:

Do not consider the corner elements i.e A[0] and A[N-1] as the answer.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        n = len(A)
        suff = [0] * n
        suff[-2] = A[-1]
        for i in range(n-3, -1, -1):
            suff[i] = min(suff[i + 1], A[i + 1])
        
        max_A = A[0]
        for i in range(1, n - 1):
            if A[i] > max_A and A[i] < suff[i]:
                return 1
            max_A = max(max_A, A[i])
        return 0