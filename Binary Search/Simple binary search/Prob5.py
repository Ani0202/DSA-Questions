'''Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is 
not found in A return [-1, -1].'''

def searchInd(A, B, searchLower = True):
    low = 0
    high = len(A) - 1
    ind = -1
    while low <= high:
        mid = (low + high) // 2
        
        if A[mid] == B:
            ind = mid
            if searchLower:
                high = mid - 1
            else:
                low = mid + 1
                
        elif A[mid] > B:
            high = mid - 1
            
        else:
            low = mid + 1
            
    return ind
    
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        i = searchInd(A, B, True)
        j = searchInd(A, B, False)
        
        return [i, j]

