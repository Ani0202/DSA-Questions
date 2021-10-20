'''Given a column title A as appears in an Excel sheet, return its corresponding column number.'''

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        n = len(A)
        ans = 0
        for i in range(n):
            t = ord(A[-1]) - ord('A') + 1
            ans += t * (26**i)
            A = A[:-1]
            
        return ans
        
