'''Given an one-dimensional unsorted array A containing N integers.

You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.

Return 1 if any such pair exists else return 0.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        B = abs(B)
        i = 0
        j = 1
        while i < len(A) and j < len(A):
            if i != j  and A[j] - A[i] == B:
                return 1
            elif A[j] - A[i] < B:
                j += 1
            else:
                i += 1
                
        return 0
