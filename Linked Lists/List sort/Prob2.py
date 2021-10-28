'''Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def partition(self, A, B):
	    head1start = None
	    head1end = None
	    head2start = None
	    head2end = None
	    while A != None:
	        if A.val < B:
	            if head1start == None:
	                head1end = head1start = A
	            else:
	                head1end.next = A
	                head1end = A
	                   
	        else:
	            if head2start == None:
	                head2end = head2start = A
	            else:
	                head2end.next = A
	                head2end = A
	                
	        A = A.next
	        
	    if head2end != None:
	        head2end.next = None
	        
	    if head1start == None:
	        return head2start
	        
	    head1end.next = head2start
	    return head1start
	        