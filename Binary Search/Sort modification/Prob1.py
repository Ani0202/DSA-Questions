'''Given an array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE:- Array A was sorted in non-decreasing order before rotation.'''

def searchPivot(A):
    low = 0
    n = len(A)
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        
        nextInd = (mid + 1)%n
        prevInd = (mid - 1 + n)%n
        
        if A[mid] < A[prevInd] and A[mid] < A[nextInd]:
            return mid
            
        elif A[mid] <= A[high]:
            high = mid - 1
            
        elif A[mid] > A[high]:
            low = mid + 1

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pivot = searchPivot(A)
        if B <= A[-1]:
            low = pivot
            high = len(A) - 1
            
        else:
            low = 0
            high = pivot - 1
            
        while low <= high:
            mid = (low + high)//2
            if A[mid] == B:
                return mid
                
            elif A[mid] > B:
                high = mid - 1
                
            else:
                low = mid + 1
                
        return -1
        
