'''Given an integer array A of size N. You need to count the number of special elements in the given array.

A element is special if removal of that element make the array balanced.

Array will be balanced if sum of even index element equal to sum of odd index element.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        leftodd = [0 for _ in range(n)]
        lefteven = [0 for _ in range(n)]
        rightodd = [0 for _ in range(n)]
        righteven = [0 for _ in range(n)]
        even = 0
        odd = 0
        for i in range(n):
            leftodd[i] = odd
            lefteven[i] = even
            if i%2 == 0:
                even += A[i]
            else:
                odd += A[i]
                
        even = 0
        odd = 0
        for i in range(n-1, -1, -1):
            rightodd[i] = odd
            righteven[i] = even
            if i%2 == 0:
                even += A[i]
            else:
                odd += A[i]
        
        count = 0        
        for i in range(n):
            if (leftodd[i] + righteven[i] == lefteven[i] + rightodd[i]):
                count = count + 1
        
        return count