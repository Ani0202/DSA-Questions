'''Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.'''

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        reversedA = 0
        temp = A
        while temp > 0:
            reversedA = (reversedA * 10) + (temp%10)
            temp = int(temp /10)
            
        if reversedA == A:
            return 1
        else:
            return 0
            
