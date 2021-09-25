'''You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        max1 = -float('inf')
        max2 = -float('inf')
        min1 = float('inf')
        min2 = float('inf')
        
        for i in range(len(A)):
            max1 = max(max1, A[i] + i)
            min1 = min(min1, A[i] + i)
            max2 = max(max2, A[i] - i)
            min2 = min(min2, A[i] - i)
            
        return(max(max1 - min1, max2 - min2))