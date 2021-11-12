'''
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

Output : 1
'''

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = str(A)
        h = dict()
        for i in range(len(A)):
            prod = int(A[i])
            
            h[prod] = h.get(prod, 0) + 1
            
            if h[prod] > 1:
                return 0
                
            for j in range(i+1, len(A)):
                prod *= int(A[j])
                h[prod] = h.get(prod, 0) + 1
            
                if h[prod] > 1:
                    return 0
                    
        return 1
