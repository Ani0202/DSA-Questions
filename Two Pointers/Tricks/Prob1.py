'''Given a binary array A and a number B, we need to find length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        p = 0
        tempLen = 0
        maxLen = 0
        for i in range(len(A)):
            if A[i] == 0:
                tempLen += 1
                
            while tempLen > B:
                if A[p] == 0:
                    tempLen -= 1
                p += 1
                
            maxLen = max(maxLen, i-p+1)
            
        return maxLen
