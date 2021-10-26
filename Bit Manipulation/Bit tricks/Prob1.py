'''Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        minXor = float('inf')
        n = len(A)
        for i in range(n-1):
            minXor = min(minXor, A[i] ^ A[i+1])
            
        return minXor
