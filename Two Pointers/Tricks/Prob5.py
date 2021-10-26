'''You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;'''

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        i = 0
        j = 0
        k = 0
        mindiff = float('inf')
        while i < len(A) and j < len(B) and k < len(C):
            mindiff = min(mindiff, max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])))
            
            t = min(A[i], B[j], C[k])
            if A[i] == t:
                i += 1
            if B[j] == t:
                j += 1
            if C[k] == t:
                k += 1
                
        return mindiff
