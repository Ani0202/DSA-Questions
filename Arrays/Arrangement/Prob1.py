'''Given a sorted array A containing N integers both positive and negative.

You need to create another array containing the squares of all the elements in A and return it in non-decreasing order.

Try to this in O(N) time.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        for m in range(len(A)):
            if A[m] >= 0:
                break
            
        i = m -1
        j = m
        ind = 0
        
        arr = [0] * len(A)
        
        while (i >= 0 and j < len(A)):
            if A[i]**2 < A[j]**2:
                arr[ind] = A[i]**2
                i = i - 1
                
            else:
                arr[ind] = A[j]**2
                j = j + 1
                
            ind = ind + 1
            
        while i >= 0:
            arr[ind] = A[i] ** 2
            i = i - 1
            ind = ind + 1
            
        while j < len(A):
            arr[ind] = A[j] ** 2
            j = j + 1
            ind = ind + 1
            
        return arr