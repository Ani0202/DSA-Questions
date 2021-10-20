'''Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

Given an array A of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array. Return the answer modulo 1000000007.'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        if len(A) <= 1:
            return 0
            
        ans = 0
        for i in range(32):
            count = 0
            for j in range(len(A)):
                if (A[j] & (1<<i)):
                    count += 1
                    
            ans += 2 * count * (len(A) - count)
           
        return ans%1000000007    
