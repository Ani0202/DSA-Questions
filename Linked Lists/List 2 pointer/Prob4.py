'''Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A == None or A.next == None:
            return A
        head = A
        while A.next != None:
            if A.val == A.next.val:
                A.next = A.next.next
            else:
                A = A.next
                
        return head
