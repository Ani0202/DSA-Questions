'''You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.'''

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        sumN = (n * (n + 1))//2
        sumNsq = ((n * (n + 1) * (2 * n + 1))//6)
        
        for i in range(n):
            sumN -= A[i]
            sumNsq -= A[i] * A[i]
            
        missNum = (sumN + sumNsq // sumN)//2
        repeatNum = missNum - sumN
        
        return [repeatNum, missNum]