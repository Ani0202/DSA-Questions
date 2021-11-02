'''Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than 
i.

More formally,

    G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        n = len(A)
        G = [0] * n
        s = []
        for i in range(n):
            while len(s) != 0 and A[i] <= s[-1]:
                s.pop()
            
            if len(s) != 0:
                G[i] = s[-1]
            else:
                G[i] = -1
            
            s.append(A[i])
            
        return G
