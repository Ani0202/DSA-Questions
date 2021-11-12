'''
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
'''

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        t = []
        ans = []
        self.allPermutations(A, t, ans)
        return ans
        
    def allPermutations(self, A, t, ans):
        if len(A) == 0:
            ans.append(list(t))
            return
        
        for i in range(len(A)):
            t.append(A[i])
            self.allPermutations(A[:i]+A[i+1:], t, ans)
            t.pop()
