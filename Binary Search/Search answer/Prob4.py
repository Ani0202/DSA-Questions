'''Given 2 integers A and B and an array of integars C of size N.

Element C[i] represents length of ith board.

You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 
unit of board.

Calculate and return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections 
of board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003'''

def isPossible(C, A, currAns):
    n = len(C)
    painters = 1
    currSum = 0
    for i in range(n):
        if C[i] > currAns:
            return False
            
        if C[i] + currSum > currAns:
            painters += 1
            currSum = C[i]
            
            if painters > A:
                return False
                
        else:
            currSum += C[i]
            
    return True

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        n = len(C)
        total = 0
        if (n < A):
            return max(C) * B
        
        for i in range(n):
            total += C[i]
            
        low = 0
        high = total
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if isPossible(C, A, mid):
                result = mid
                high = mid - 1
                
            else:
                low = mid + 1
                
        return (result * B) % 10000003

