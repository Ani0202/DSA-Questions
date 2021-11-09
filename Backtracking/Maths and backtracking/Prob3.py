'''The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must 
begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
There might be multiple gray code sequences possible for a given n.
Return any such sequence.'''

def generateGrayCode(A):
    if A <= 0:
        return ['0']
    if A == 1:
        return ['0', '1']
            
    recAns = generateGrayCode(A-1)
        
    ans = []
        
    for i in range(len(recAns)):
        s = recAns[i]
        ans.append('0' + s)
            
    for i in range(len(recAns) - 1, -1, -1):
        s = recAns[i]
        ans.append('1' + s)
            
    return ans

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        B=[int(k,2) for k in generateGrayCode(A)]
        return(B)
        