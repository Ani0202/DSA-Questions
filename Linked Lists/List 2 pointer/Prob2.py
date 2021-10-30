'''Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        newHead = prev = ListNode(None)
        newHead.next = head
        while head and head.next:
            if head.val == head.next.val:
                while (head and head.next and head.val == head.next.val):
                    head = head.next
                
                head = head.next
                prev.next = head
                
            else:
                prev = prev.next
                head = head.next
                
        return newHead.next
            
