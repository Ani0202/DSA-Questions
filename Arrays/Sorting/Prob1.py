'''Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals 
to p.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A=sorted(A)
        n=len(A)
        if A[-1]==0:
            return 1
           
            
        for i in range(n-1):
            if A[i]==A[i+1]:
                continue
            elif A[i]==n-i-1:
                return 1
        return -1