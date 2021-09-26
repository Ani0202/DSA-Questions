'''You are given a 1D integer array B containing A integers.

Count the number of ways to split all the elements of the array into 3 contiguous parts so that the sum of elements in each part is the same.

Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n])'''

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        cnt = [0 for _ in range(A)]
        s = sum(B)
        ans = 0
 
        if (s % 3 != 0):
            return 0
 
        s = s / 3
 
        ss = 0
        
        for i in range(A-2):
            ss = ss + B[i]
            if ss == s:
                cnt[i+1] = cnt[i] + 1
            else:
                cnt[i+1] = cnt[i]
                
        ss = 0
        for i in range(A - 1, 1, -1):
            ss = ss + B[i]
            if ss == s:
                ans = ans + cnt[i-1]
        return ans