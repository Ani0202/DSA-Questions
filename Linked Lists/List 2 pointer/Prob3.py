'''Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        newList = ListNode(None)
        head = newList
        while True:
            if A == None:
                newList.next = B
                break
            if B == None:
                newList.next = A
                break
            if A.val < B.val:
                newList.next = A
                A = A.next
                newList = newList.next
            else:
                newList.next = B
                B = B.next
                newList = newList.next
                
        return head.next
