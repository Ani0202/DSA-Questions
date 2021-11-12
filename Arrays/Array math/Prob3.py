'''There is a corridor in a Jail which is N units long. Given an array A of size N. The ith index of this array is 0 if the light at ith 
position is faulty otherwise it is 1.

All the lights are of specific power B which if is placed at position X, it can light the corridor from [ X-B+1, X+B-1].

Initially all lights are off.

Return the minimum number of lights to be turned ON to light the whole corridor or -1 if the whole corridor cannot be lighted.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        
        i=0
        count=0
        len_a=len(A)
        while(i<len_a):
            j=min(i+B-1,len_a-1)
            found=False
            while(j>min((i-B+1),0)):
                if(A[j]==1):
                    found=True
                    count+=1
                    i=j+B
                    break
                j = j -1
            if not found:
                return -1
        return count
