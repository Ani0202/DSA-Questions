'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.
'''

class Solution:
    	# @param A : integer
	# @return a list of strings
	def generateParenthesis(self, A):
	    t = [""] * 2 * A
	    ans = []
	    o = 0
	    c = 0
	    self.allparen(t, 0, A, 0, 0, ans)
	    return ans
	    
	def allparen(self, t, pos, A, o, c, ans):
	    if c == A:
	        ans.append(''.join(t))
	        return
	    
	    if o < A:
	        t[pos] = '('
	        self.allparen(t, pos+1, A, o+1, c, ans)
	    
	    if o > c:
	        t[pos] = ')'
	        self.allparen(t, pos+1, A, o, c+1, ans)