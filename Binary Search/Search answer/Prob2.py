'''Given an integer A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.

NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.'''

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        #nums = list(range(A+1))
        low = 1
        high = A
        prevSqrt = A
        while low <= high:
            mid = (low + high)//2
            if mid * mid == A:
                return mid
            elif mid * mid > A:
                high = mid - 1
            else:
                prevSqrt = mid
                low = mid + 1
                
        return prevSqrt
