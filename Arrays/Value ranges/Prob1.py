'''Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

NOTE: You should make minimum number of comparisons.'''

def min_max(A, l, h):
    if l == h:
        return (A[l], A[h])
    
    elif h == l + 1:
        if A[h] >= A[l]:
            return (A[l], A[h])
        else:
            return (A[h], A[l])
            
    else:
        m = int(l + (h-l)/2)
        min1, max1 = min_max(A, l, m)
        min2, max2 = min_max(A, m+1, h)
        return (min(min1, min2), max(max1, max2))
        
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min_A, max_A = min_max(A, 0, len(A) - 1)
        return min_A + max_A
