'''Given an array A containing N integers.

You need to find the maximum sum of triplet ( Ai + Aj + Ak ) such that 0 <= i < j < k < N and Ai < Aj < Ak.

If no such triplet exist return 0.'''

from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        max_right = [0] * n
        max_right[-1] = A[-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], A[i])
        min_left = []
        ans = 0
        min_left.append(A[0])
        for i in range(1, n-1):
            left_ind = BinarySearch(min_left, A[i])
            if(left_ind!=-1):
                if max_right[i + 1] <= A[i]:
                    continue
                temp_ans = min_left[left_ind] + A[i] + max_right[i+1]
                ans = max(ans, temp_ans)
            min_left.insert(left_ind + 1, A[i])
        return ans