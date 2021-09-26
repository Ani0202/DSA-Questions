'''Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A = ''.join([str(i) for i in A])
        A = int(A) + 1
        return list(str(A))