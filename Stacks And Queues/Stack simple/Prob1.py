'''Given a string A consisting only of '(' and ')'.

You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []
        n = len(A)
        for i in range(n):
            if A[i] == '(':
                stack.append(A[i])
            else:
                if len(stack) == 0:
                    return 0
                stack.pop()
                
        if len(stack) == 0:
            return 1
        else:
            return 0
