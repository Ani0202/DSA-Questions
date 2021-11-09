'''
Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
'''

class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        t = []
        ans = []
        self.findpalind(A, t, ans, 0)
        return ans
        
    def findpalind(self, A, t, ans, ind):
        if ind >= len(A):
            ans.append(list(t))
            return
        
        for i in range(ind, len(A)):
            if self.isPalind(A, ind, i):
                t.append(A[ind:i+1])
                self.findpalind(A, t, ans, i + 1)
                t.pop()
                
    def isPalind(self, st, l, h):
        while l < h:
            if st[l] != st[h]:
                return False
            l += 1
            h -= 1
        return True