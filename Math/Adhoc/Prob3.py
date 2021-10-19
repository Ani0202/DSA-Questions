'''Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.'''

class Solution:
    	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
	    primes = [True] * (A+1)
	    i = 2
	    while i*i <= A:
	        if primes[i]:
	            for j in range(i*i, A+1, i):
	                primes[j] = False
	                
	        i += 1
	        
	    for i in range(2, A+1):
	        if(primes[i] and primes[A-i]):
	            return [i, A-i]