'''Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.'''

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        n = len(A)
        
        st = []
        for i in range(n):
            if A[i] != '/' and A[i] != '*' and A[i] != '-' and A[i] != '+':
                st.append(A[i])
            else:
                b = int(st.pop())
                a = int(st.pop())
                if A[i] == '/':
                    t = str(a/b)
                elif A[i] == '*':
                    t = str(a*b)
                elif A[i] == '-':
                    t = str(a-b)
                else:
                    t = str(a+b)
                st.append(t)
                
        return int(st[-1])
                
