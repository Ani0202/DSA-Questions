'''You are given an integer N and the task is to reverse the digits of the given integer. Return 0 if the result overflows and does not fit in a 32 bit signed integer'''

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        t = abs(A)
        r = 0
        while t > 0:
            r = r*10 + t%10
            t = int(t/10)
            if r >= 2147483647:
                return 0
            
        if A < 0:
            return -r
        return r


