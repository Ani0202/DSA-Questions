'''Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).'''

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        for length in reversed(range(len(A)+1)):
            for start in range(len(A)-length):
                window = A[start:start+length+1]
                if window==window[::-1]:
                    return window
