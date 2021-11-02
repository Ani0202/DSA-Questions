'''Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

Absolute path always begin with ’/’ ( root directory ).

Path will not have whitespace characters.'''

class Solution:
    	# @param A : string
	# @return a strings
	def simplifyPath(self, A):
	    st = []
	    res = "/"
	    n = len(A)
	    i = 0
	    while i < n:
	        dirStr = ""
	        while i < n and A[i] == '/':
	            i += 1
	            
	        while i < n and A[i] != '/':
	            dirStr += A[i]
	            i += 1
	            
	        if dirStr == '..':
	            if len(st):
	                st.pop()
	        elif dirStr == '.':
	            continue
	        elif len(dirStr) > 0:
	            st.append(dirStr)
	            
	        i += 1
	        
	    st1 = []
	    while len(st):
	        st1.append(st[-1])
	        st.pop()
	        
	    while len(st1):
	        temp = st1[-1]
	        if (len(st1) != 1):
	            res += (temp + "/")
	        else:
	            res += temp
	            
	        st1.pop()
	        
	    return res
