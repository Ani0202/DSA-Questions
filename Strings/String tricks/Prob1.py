'''Given an string A. The only operation allowed is to insert characters in the beginning of the string.

Find how many minimum characters are needed to be inserted to make the string a palindrome string.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        A = A + '$' + A[::-1]
        lps = [0] * len(A)
        i = 1
        l = 0
        while i < len(A):
            if A[i] == A[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
                    
        return n - lps[-1]
            
