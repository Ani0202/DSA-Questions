'''Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        if (A<0) ^ (B<0):
            sign = -1
        else:
            sign = 1
            
        A = abs(A)
        B = abs(B)
        
        q = 0
        t = 0
        
        for i in range(31, -1, -1):
            if(t + (B<<i) <= A):
                t += B<<i
                q = q | (1<<i)
                
        q = q * sign
        
        if q > 2**31 - 1:
            return 2**31 -1
                
        return q
