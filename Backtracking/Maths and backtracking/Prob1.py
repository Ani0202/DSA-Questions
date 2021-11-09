'''Given a string A and integer B, what is maximal lexicographical stringthat can be made from A if you do atmost B swaps.'''

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        if B<=0:
            return A
        x=list(A)
        if x==sorted(x,reverse=True):
            return A
        y=''
        n=len(x)
        for i in range(n):
            for j in range(i+1,n):
                z=''.join(x[:i]+x[j:j+1]+x[i+1:j]+x[i:i+1]+x[j+1:])
                y=max(y,self.solve(z,B-1))
        return y