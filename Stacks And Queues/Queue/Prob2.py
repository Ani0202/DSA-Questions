'''Given an array of integers A. There is a sliding window of size B which
is moving from the very left of the array to the very right.
You can only see the w numbers in the window. Each time the sliding window moves
rightwards by one position. You have to find the maximum for each window.
The following example will give you more clarity.

The array A is [1 3 -1 -3 5 3 6 7], and B is 3.

Window position	Max
———————————-	————————-
[1 3 -1] -3 5 3 6 7	3
1 [3 -1 -3] 5 3 6 7	3
1 3 [-1 -3 5] 3 6 7	5
1 3 -1 [-3 5 3] 6 7	5
1 3 -1 -3 [5 3 6] 7	6
1 3 -1 -3 5 [3 6 7]	7
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

Note: If B > length of the array, return 1 element with the max of the array.'''

from collections import deque

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        if B >= len(A):
            return [max(A)]
        Q = deque()
        for i in range(B):
            while Q and A[i] >= A[Q[-1]]:
                Q.pop()
            Q.append(i)
        
        ans = []  
        for i in range(B, len(A)):
            ans.append(A[Q[0]])
            
            while Q and Q[0] <= i - B:
                Q.popleft()
                
            while Q and A[i] >= A[Q[-1]]:
                Q.pop()
                
            Q.append(i)
            
        ans.append(A[Q[0]])
        
        return ans