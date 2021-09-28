'''Given numRows, generate the first numRows of Pascal's triangle.
Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 0:
            return []
        triangle = [[1]]
        if A == 1:
            return triangle
        for i in range(1, A):
            tmp=[1]
            for j in range(1,i):
                tmp.append(triangle[i-1][j-1]+triangle[i-1][j])
            tmp.append(1)
            triangle.append(tmp)
        return triangle