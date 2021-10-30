'''Sort a linked list using insertion sort.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head = A
        while head != None:
            P = A
            while P != head:
                if P.val > head.val:
                    P.val, head.val = head.val, P.val
                else:
                    P = P.next
                    
            head = head.next
        
        return A