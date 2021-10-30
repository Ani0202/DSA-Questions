'''Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        head = A
        l = 1
        while A.next != None:
            l += 1
            A = A.next
            
        A.next = head
        B = B % l
        head1 = head
        while l-1 > B:
            head = head.next
            l -= 1
            
        ans = head.next
        head.next = None
        
        return ans
