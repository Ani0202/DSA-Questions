'''Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.'''

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        i = 0
        j = len(A) - 1
        while i <= j:
            if not A[i].isalnum():
                i += 1
            elif not A[j].isalnum():
                j -= 1
            elif A[i].lower() != A[j].lower():
                return 0
            else:
                i += 1
                j -= 1
                
        return 1
