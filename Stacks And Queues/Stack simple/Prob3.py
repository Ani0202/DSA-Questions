'''Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.

Chech whether A has redundant braces or not.

Return 1 if A has redundant braces, else return 0.

Note: A will be always a valid expression.'''

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for i in A:
            if i == ')':
                top = stack[-1]
                flag = True
                while top != '(':
                    if (top == '+' or top == '-' or top == '*' or top == '/'):
                        flag = False
                    stack.pop()
                    top = stack[-1]
                    
                stack.pop()
                
                if flag:
                    return 1
                    
            else:
                stack.append(i)
                
        return 0
