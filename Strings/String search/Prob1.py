'''You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans = 0
        n = len(A)
        vowels = list('aeiouAEIOU')
        for i in range(n):
            if A[i] in vowels:
                ans += (n - i)
                
        return ans % 10003
