'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
The solution set must not contain duplicate combinations.
Example,
Given candidate set 2,3,6,7 and target 7,
A solution set is:

[2, 2, 3]
[7]
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        ans = []
        t = []
        A = sorted(list(set(A)))
        self.findSum(ans, A, t, B, 0)
        return ans
        
    def findSum(self, ans, A, t, B, ind):
        if B == 0:
            ans.append(list(t))
            return
        
        for i in range(ind, len(A)):
            if B - A[i] >= 0:
                t.append(A[i])
                self.findSum(ans, A, t, B - A[i], i)
                
                t.remove(A[i])
