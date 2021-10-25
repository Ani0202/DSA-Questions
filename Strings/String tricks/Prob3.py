'''Given a string A consisting of lowercase characters.

We need to tell minimum characters to be appended (insertion at end) to make the string A a palindrome.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        A = A[::-1] + '$' + A
        i = 1
        l = 0
        lps = [0] * len(A)
        while i < len(A):
            if A[i] == A[l]:
                l = l + 1
                lps[i] = l
                i = i + 1
            else:
                if l == 0:
                    lps[i] = 0
                    i = i + 1
                    
                else:
                    l = lps[l-1]
                    
        return n - lps[-1]