'''Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".'''

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        minLen = float('inf')
        n = len(A)
        minLenInd = -1
        for i in range(n):
            if len(A[i]) < minLen:
                minLen = len(A[i])
                minLenInd = i
        
        ans = ''
        for i in range(minLen):
            a = A[minLenInd][i]
            for j in range(n):
                if A[j][i] != a:
                    return ans
                    
            ans = ans + a
            
        return ans
        
