'''Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level 
revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        A = list(map(int, A.split('.')))
        B = list(map(int, B.split('.')))
        n = len(A)
        m = len(B)
        i = 0
        j = 0
        while i < n or j < m:
            if i >= n:
                a = 0
            else:
                a = A[i]
                
            if j >= m:
                b = 0
            else:
                b = B[j]
                
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                i = i + 1
                j = j + 1
                
        return 0