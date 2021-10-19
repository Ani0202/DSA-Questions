'''Given the position of a Bishop (A, B) on an 8 * 8 chessboard.

Your task is to count the total number of squares that can be visited by the Bishop in one move.

The position of the Bishop is denoted using row and column number of the chessboard.'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        d1 = min(A, B) - 1
        d2 = 8 - max(A, B)
        d3 = min(A, 9-B) -1
        d4 = 8 - max(A, 9-B)
        return d1 + d2 + d3 + d4
        
