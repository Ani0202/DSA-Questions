'''Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.'''

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        conv = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        ans = 0

        i = 0
        
        while i < len(A):
            s1 = conv[A[i]]
            
            if (i < len(A) - 1):
                s2 = conv[A[i+1]]
                
                if (s1 >= s2):
                    ans += s1
                    
                    i += 1
                else:
                    ans += (s2 - s1)
                    
                    i += 2
            else:
                ans += s1
                
                i += 1
        
        return ans
