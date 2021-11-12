'''
Given an integer array A of size N, find the first repeating element in it.

We need to find the element that occurs more than once and whose index of first occurrence is smallest.

If there is no repeating element, return -1.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ansInd = n
        hMap = dict()
        
        for i in range(n):
            hMap[A[i]] = hMap.get(A[i], 0) + 1
            
        for i in range(n):
            if hMap[A[i]] > 1:
                return A[i]
                
        return -1
                
