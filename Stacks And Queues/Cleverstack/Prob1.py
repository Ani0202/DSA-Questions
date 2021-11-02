'''You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the 
following:

LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] and (i>j). If multiple A[j]'s are present in multiple 
positions, the LeftSpecialValue is the maximum value of j.
RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] and (j>i). If multiple A[j]'s are present in multiple 
positions, the RightSpecialValue is the minimum value of j.
Write a program to find the maximum special product of any integer in the array.

NOTE: As the answer can be large, output your answer modulo 109 + 7.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        n = len(A)
        left = [0] * n
        s = []
        for i in range(n):
            while len(s) != 0 and A[i] >= A[s[-1]]:
                s.pop()
                
            if len(s) != 0:
                left[i] = s[-1]
            else:
                left[i] = 0
                
            s.append(i)
            
        s = []
        right = [0] * n
        for i in  range(n-1, -1, -1):
            while len(s) != 0 and A[i] >= A[s[-1]]:
                s.pop()
                
            if len(s) != 0:
                right[i] = s[-1]
            else:
                right[i] = 0
                
            s.append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans, left[i]*right[i])%1000000007
            
        return ans
