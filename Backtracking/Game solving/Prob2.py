'''Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.



A sudoku puzzle,



and its solution numbers marked in red.

Example :

For the above given diagrams, the corresponding input to your program will be

[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
and we would expect your program to modify the above array of array of characters to

[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]
'''
class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, board):
        
        empty = [-1,-1]
        if not self.find_empty_location(board,empty):
            return True
        
        r,c = empty[0],empty[1]
        
        for num in range(1,10):
            if self.isvalid(num, r, c, board):
                board[r][c] = str(num)

                if self.solveSudoku(board):
                    return True
                board[r][c] = '.'
             
    def find_empty_location(self, board, empty):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty[0] = i
                    empty[1] = j
                    return True
        return False
    
    def isvalid(self, num, r, c, board):
        for i in range(9):
            if board[i][c] == str(num):
                return False
        for j in range(9):
            if board[r][j] == str(num):
                return False
        r = r-r%3
        c = c-c%3
        for i in range(3): 
            for j in range(3): 
                if board[i+r][j+c] == str(num): 
                    return False
        return True
