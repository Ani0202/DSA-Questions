'''You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant 
additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        c1 = 0
        c2 = 0
        m1 = '0'
        m2 = '0'
        for i in A:
            if m1 == i:
                c1 += 1
            elif m2 == i:
                c2 += 1
            elif c1 == 0:
                m1 = i
                c1 += 1
            elif c2 == 0:
                m2 = i
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
                
        c1 = 0
        c2 = 0
                
        for i in A:
            if m1 == i:
                c1 += 1
            elif m2 == i:
                c2 += 1
                
        if c1 > n/3:
            return m1
        
        elif c2 > n/3:
            return m2
            
        else:
            return -1
