'''Given a string A consisting of lowercase characters.

You have to find the number of substrings in A which starts with vowel and end with consonants or vice-versa.

Return the count of substring modulo 109 + 7.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) == 0:
            return 0
        vowels = 'aeiou'
        c = 0
        v = 0
        ans = 0
        if A[-1] in vowels:
            v += 1
        else:
            c += 1
            
        for i in range(len(A) - 2, -1, -1):
            if A[i] in vowels:
                ans += c
                v += 1
            else:
                ans += v
                c += 1
                
        return ans % 1000000007
