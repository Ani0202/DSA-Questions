'''Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.'''

def pivotIndex(A):
    low = 0
    n = len(A)
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        
        nextInd = (mid + 1)%n
        prevInd = (mid - 1 + n)%n
        if (A[mid] > A[nextInd]) and (A[mid] > A[prevInd]):
            return mid
            
        elif A[mid] > A[prevInd] and A[mid] < A[nextInd]:
            low = mid + 1
            
        elif A[mid] < A[prevInd] and A[mid] > A[nextInd]:
            high = mid - 1
            
def binarySearch(A, B, r):
    low = 0
    n = len(A)
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        
        if A[mid] == B:
            return mid
            
        elif A[mid] > B:
            if r:
                low = low + 1
            else:
                high = high - 1
                
        else:
            if r:
                high = high - 1
            else:
                low = low + 1
                
    return -1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = pivotIndex(A)
        
        ind1 = binarySearch(A[:i], B, False)
        ind2 = binarySearch(A[i:], B, True)
        if ind1 == -1:
            if ind2 == -1:
                return -1
            else:
                return i + ind2
            
        return ind1
