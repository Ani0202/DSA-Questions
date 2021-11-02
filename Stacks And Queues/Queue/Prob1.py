'''Given a string A denoting a stream of lowercase alphabets. You have to make new string B.

B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the 
end to B. If no non-repeating character is found then append '#' at the end of B.'''

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        a = []
        count = {}
        n = len(A)
        ans = ''
        for i in range(n):
            count[A[i]] = count.get(A[i], 0) + 1
            a.append(A[i])
            
            while len(a) != 0:
                if count[a[0]] > 1:
                    del a[0]
                else:
                    ans += a[0]
                    break
                    
            if len(a) == 0:
                ans += '#'
                
        return ans
