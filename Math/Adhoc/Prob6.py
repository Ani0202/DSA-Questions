'''Given four positive integers A, B, C, D, determine if there’s a rectangle such that the lengths of its sides are A, B, C and D (in any order).

If any such rectangle exist return 1 else return 0.'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        if A == B:
            if C == D:
                return 1
            else:
                return 0
                
        if A == C:
            if B == D:
                return 1
            else:
                return 0
                
        if A == D:
            if B == C:
                return 1
            else:
                return 0
                
        return 0
                
        
        
