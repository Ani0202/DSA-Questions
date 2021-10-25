'''Given a string A consisting only of lowercase characters, we need to check whether it is possible to make this string a palindrome after 
removing exactly one character from this.

If it is possible then return 1 else return 0.'''

def isPalin(A):
    if A == A[::-1]:
        return 1
    return 0

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        i = 0
        j = n - 1
        while i <= j:
            if A[i] != A[j]:
                if isPalin(A[i:j]):
                    return 1
                if isPalin(A[i+1:j+1]):
                    return 1
                return 0
                
            else:
                 i += 1
                 j -= 1
                
        if n%2 != 0:
            return 1
        return 0