'''
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.



The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

 Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        A = [list(i) for i in A]
        for i in range(9):
            hMap = {}
            for j in range(9):
                if A[i][j] != '.':
                    hMap[A[i][j]] = hMap.get(A[i][j], 0) + 1
                    if hMap[A[i][j]] > 1:
                        return 0
                    
            hMap = {}
            for j in range(9):
                if A[j][i] != '.':
                    hMap[A[j][i]] = hMap.get(A[j][i], 0) + 1
                    if hMap[A[j][i]] > 1:
                        return 0
            
            hMap = {}
            r = 3 * (i%3)
            c = 3 * (i//3)
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if A[i][j] != '.':
                        hMap[A[i][j]] = hMap.get(A[i][j], 0) + 1
                        if hMap[A[i][j]] > 1:
                            return 0
                        
        return 1