'''Given an array A of positive integers,call a (contiguous,not necessarily distinct) subarray of A good if the number of different integers 
in that subarray is exactly B.

(For example: [1, 2, 3, 1, 2] has 3 different integers 1, 2 and 3)

Return the number of good subarrays of A.'''

def atMostK(A, B):
    count = 0
    l = 0
    r = 0
    hist = dict()
    
    while r < len(A):
        hist[A[r]] = hist.get(A[r], 0) + 1
        
        while len(hist) > B:
            hist[A[l]] = hist.get(A[l], 0) - 1
            
            if hist[A[l]] == 0:
                del hist[A[l]]
                
            l += 1
            
        count += r - l + 1
        r += 1
    
    return count

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return (atMostK(A, B) - atMostK(A, B-1))
        
