'''
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2
Output :

1
as 3 - 1 = 2

Return 0 / 1 for this problem.
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        hMap = dict()
        n = len(A)
        for i in range(n):
            if A[i] in hMap:
                hMap[A[i]].append(i)
            else:
                hMap[A[i]] = [i]
            
        for i in range(n):
            if A[i] - B in hMap:
                for j in hMap[A[i] - B]:
                    if i != j:
                        return 1
                        
        return 0