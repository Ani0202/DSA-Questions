'''Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

 Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        head = A
        head1 = head
        count = 0
        while A != None:
            count += 1
            A = A.next
            
        if B >= count:
            return head.next
            
        while head != None and count != B+1:
            count -= 1
            head = head.next
            
        head.next = head.next.next
        
        return head1
