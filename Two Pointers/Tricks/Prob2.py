'''Given an array A of N non-negative numbers and you are also given non-negative number B.

You need to find the number of subarrays in A having sum less than B. We may assume that there is no overflow.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = 0
        j = 0
        ans = 0
        s = A[0]
        
        while i < len(A) and j < len(A):
            if s < B:
                j += 1
                if j >= i:
                    ans += j - i
                    
                if j < len(A):
                    s += A[j]
                    
            else:
                s -= A[i]
                i += 1
                
        return ans
