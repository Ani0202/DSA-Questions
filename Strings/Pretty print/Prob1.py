'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern 
in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B == 1:
            return A
        r = 0
        n = len(A)
        ans = [''] * B
        for i in range(n):
            ans[r] += A[i]
            
            if r == B-1:
                direc = 'up'
                
            elif r == 0:
                direc = 'down'
                    
            if direc == 'down':
                r += 1
                
            else:
                r -= 1
                
        return ''.join(ans)
                
