'''Given two binary strings, return their sum (also a binary string).'''

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        n = max(len(A), len(B))
        A = '0' * (n-len(A)) + A
        B = '0' * (n-len(B)) + B
        
        carry = 0
        ans = ''
        for i in range(n-1, -1, -1):
            t = carry
            if A[i] == '1':
                t += 1
            if B[i] == '1':
                t += 1
                
            if t % 2 == 1:
                ans += '1'
            else:
                ans += '0'
            
            if t < 2:
                carry = 0
            else:
                carry = 1
                
        if carry != 0:
            ans += '1'
            
        return ans[::-1]