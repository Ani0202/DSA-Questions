'''You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.

Example:

Input : 
Array = {1 1 0 1 1 0 0 1 1 1 } 
M = 1

Output : 
[0, 1, 2, 3, 4] 

If there are multiple possible solutions, return the sequence which has the minimum start index.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        p = 0
        ap = 0
        tempLen = 0
        maxLen = 0
        for i in range(len(A)):
            if A[i] == 0:
                tempLen += 1
                
            while (tempLen > B):
                if A[p] == 0:
                    tempLen -= 1
                p += 1
            
            if maxLen < i-p+1:
                ap = p
                
                maxLen = i-p+1
            
        return list(range(ap, ap + maxLen))
