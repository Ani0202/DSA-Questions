'''Given an index k, return the kth row of the Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Input : k = 3


Return : [1,3,3,1]

Note: k is 0 based. k = 0, corresponds to the row [1].'''

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        prev = 1
        ans = list()
        ans.append(prev)
        for i in range(1, A+1):
            curr = (prev * (A - i + 1)) // i
            ans.append(curr)
            prev = curr
        return ans
            
