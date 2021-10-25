'''Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. '''

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        if A == '0' or B == '0':
            return '0'
            
        A = A[::-1]
        B = int(B)
        carry = 0
        ans = ''
        for i in range(len(A)):
            prod = int(A[i]) * B + carry
            n = prod % 10
            carry = prod//10
            ans = str(n) + ans
            
        if carry >0:
            ans = str(carry) + ans
            
        return ans
            
        
