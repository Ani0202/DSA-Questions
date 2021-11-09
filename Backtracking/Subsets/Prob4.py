'''
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        t = []
        ans = []
        self.combination(A, B, t, ans, 0)
        return ans
        
    def combination(self, A, B, t, ans, ind):
        if B == 0:
            ans.append(list(t))
            return
        
        for i in range(ind, A):
            if B - 1 >= 0:
                t.append(i+1)
                self.combination(A, B-1, t, ans, i + 1)
                t.pop()
