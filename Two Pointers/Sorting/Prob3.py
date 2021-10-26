'''Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2) '''

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        if len(A) < 3:
            return []
        
        ans = []
        A.sort()
        for i in range(len(A) - 2):
            if i != 0 and A[i] == A[i - 1]:
                continue
            
            p = i + 1
            q = len(A) - 1
            
            while p < q:
                s = A[i] + A[p] + A[q]
                if s > 0:
                    q -= 1
                elif s < 0:
                    p += 1
                else:
                    ans.append([A[i], A[p], A[q]])
                    while p < q and A[p] == A[p+1]:
                        p += 1
                    p += 1
                    
                    while p < q and A[q] == A[q-1]:
                        q -= 1
                    q -= 1
                    
        return ans
                    