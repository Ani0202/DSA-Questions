'''Given a collection of integers that might contain duplicates, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [1,2,2], the solution is:

[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
'''

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        t = []
        ans = []
        A.sort()
        self.subsets(A, t, ans, 0)
        return ans
        
    def subsets(self, A, t, ans, ind):
        ans.append(list(t))
        
        for i in range(ind, len(A)):
            if i>ind and A[i] == A[i-1]:
                continue
            t.append(A[i])
            self.subsets(A, t, ans, i+1)
                
            t.pop()