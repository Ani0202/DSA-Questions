'''Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        closetSum = float('inf')
        for i in range(len(A) - 2):
            p = i + 1
            q = len(A) - 1
            
            while p < q:
                s = A[i] + A[p] +A[q]
                
                if(abs(B - s) < abs(B - closetSum)):
                    closetSum = s
                    
                if s > B:
                    q -= 1
                else:
                     p += 1
                     
        return closetSum
