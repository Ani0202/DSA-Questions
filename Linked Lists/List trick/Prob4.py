'''Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        slow = A
        fast = slow.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        node1 = A
        node2 = slow.next
        slow.next = None
        
        prev  =None
        curr = node2
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        node2 = prev
        
        node = ListNode(None)
        curr = node
        
        while node1 != None or node2 != None:
            if node1 != None:
                curr.next = node1
                curr = curr.next
                node1 = node1.next
                
            if node2 != None:
                curr.next = node2
                curr = curr.next
                node2 = node2.next
                
        return node.next