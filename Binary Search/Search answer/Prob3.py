'''Given an array of integers A of size N and an integer B.

College library has N bags,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.'''

def isPossible(A, B, currAns):
    students = 1
    currSum = 0
    n = len(A)
    
    for i in range(n):
        if A[i] > currAns:
            return False
            
        if currSum + A[i] > currAns:
            students += 1
            currSum = A[i]
            
            if students > B:
                return False
                
        else:
            currSum += A[i]
            
    return True
    
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        total = 0
        n = len(A)
        
        if n < B:
            return -1
            
        for i in range(n):
            total += A[i]
            
        low = 0
        high = total
        result = -1
        
        while low <= high:
            mid = (low + high)//2
            if isPossible(A, B, mid):
                result = mid
                high = mid - 1
                
            else:
                low = mid + 1
                
        return result
