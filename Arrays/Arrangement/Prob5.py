'''Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater.'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        i = 1
        j = B
        ans = list()
        for k in A:
            if k == 'I':
                ans.append(i)
                i = i + 1
            else:
                ans.append(j)
                j = j - 1
        ans.append(i)
        return ans