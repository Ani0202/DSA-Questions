'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to 
T.

Each number in C may only be used once in the combination.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :

Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        ans = []
        t = []
        A = sorted(A)
        self.findSum(ans, t, A, B, 0)
        return ans
        
    def findSum(self, ans, t, A, B, ind):
        if B == 0:
            ans.append(list(t))
            return
        
        for i in range(ind, len(A)):
            if i>ind and A[i] == A[i-1]:
                continue
            if B - A[i] >= 0:
                t.append(A[i])
                self.findSum(ans, t, A, B-A[i], i+1)
                
                t.pop()
