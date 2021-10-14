'''Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        L_min = [0] * n
        R_max = [0] * n
        L_min[0] = A[0]
        R_max[-1] = A[-1]
        for i in range(1, n):
            L_min[i] = min(L_min[i-1], A[i])
        for i in range(n-2, -1, -1):
            R_max[i] = max(R_max[i+1], A[i])
            
        i, j = 0, 0
        max_diff = 0
        while i < n and j < n:
            if L_min[i] <= R_max[j]:
                max_diff = max(max_diff, j - i)
                j = j + 1
            else:
                i = i + 1
                
        return max_diff
                