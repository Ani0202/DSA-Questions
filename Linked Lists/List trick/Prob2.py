'''Given a linked list A of length N and an integer B.

You need to reverse every alternate B nodes in the linked list A.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def reverse(head, k):
    if head == None:
        return head
    count = 0
    prev = None
    curr = head
    while curr != None and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
        count += 1
        
    head.next = curr
    if curr == None:
        return prev
    p = None
    while curr != None and count > 0:
        p = curr
        curr = curr.next
        count -= 1
        
    p.next = reverse(curr, k)
    
    return prev

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        return reverse(A, B)
