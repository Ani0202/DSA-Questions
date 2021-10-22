'''Given an sorted array A of size N. Find number of elements which are less than or equal to B.

NOTE: Expected Time Complexity O(log N)'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        low = 0
        n = len(A)
        high = n - 1
        ind = -1
        while low <= high:
            mid = (low + high)//2
            if A[mid] == B:
                ind = mid
                low = mid + 1
            elif A[mid] < B:
                ind = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ind + 1
