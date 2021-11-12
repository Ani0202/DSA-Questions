'''
Find the largest continuous sequence in a array which sums to zero.

Example:


Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}

 NOTE : If there are multiple correct answers, return the sequence which occurs first in the array. 
 '''
 
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, A):
	    hMap = {0: -1}
	    s = 0
	    start = 0
	    end = 0
	    for i in range(len(A)):
	        s += A[i]
	        if s in hMap:
	            if i - hMap[s] > end - start:
	                end = i
	                start = hMap[s]
	        else:
	            hMap[s] = i
	            
	    return A[start+1:end+1]