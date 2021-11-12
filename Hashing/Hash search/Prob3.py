'''
Given an integer array A of size N containing 0's and 1's only. 

You need to find the length of the longest subarray having count of 1’s one more than count of 0’s.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hMap = dict()
        s = 0
        ans = 0
        
        for i in range(len(A)):
            if A[i] == 0:
                s -= 1
            else:
                s += 1
                
            if s == 1:
                ans = i + 1
                
            elif s not in hMap:
                hMap[s] = i
                
            if (s - 1) in hMap:
                ans = max(ans, i-hMap[s-1])
                
        return ans
