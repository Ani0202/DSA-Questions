'''Given a string A.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.

Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.

If there are multiple spaces between words, reduce them to a single space in the reversed string.'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A.split()
        A.reverse()
        return(" ".join(A))
        
