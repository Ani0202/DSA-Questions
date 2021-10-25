'''Given a string A of parantheses ‘(‘ or ‘)’.

The task is to find minimum number of parentheses ‘(‘ or ‘)’ (at any positions) we must add to make the resulting parentheses string valid.

An string is valid if:

Open brackets must be closed by the corresponding closing bracket.
Open brackets must be closed in the correct order.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        oP = 0
        cP = 0
        ans = 0
        n = len(A)
        for i in range(n):
            if A[i] == '(':
                oP += 1
            else:
                cP += 1
                if cP > oP:
                    ans += 1
                    oP += 1
                    
        return ans + oP - cP
