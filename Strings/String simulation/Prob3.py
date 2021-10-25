'''Given a string A and integer B, remove all consecutive same characters that have length exactly B.'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        n = len(A)
        if n == 1:
            if B == 1:
                return ''
            else:
                return A
        suff = [0] * n
        suff[-1] = 1
        for i in range(n-2, -1, -1):
            if A[i] == A[i + 1]:
                suff[i] = suff[i+1] + 1
                
            else:
                suff[i] = 1
                
        ans = ''
        i = 0
        while i < n:
            if suff[i] == B:
                i = i + B
            else:
                ans = ans + (A[i] * suff[i])
                i = i + suff[i]
                
        return ans
