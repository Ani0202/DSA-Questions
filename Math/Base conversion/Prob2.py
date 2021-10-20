'''Given a positive integer A, return its corresponding column title as appear in an Excel sheet.'''

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        while A > 0:
            r = A%26
            ans += alpha[r-1]
            if r != 0:
                A = int(A/26)
            else:
                A = int(A/26) - 1
            
        return ans[::-1]