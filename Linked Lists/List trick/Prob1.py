'''Given a linked list A of length N and an integer B.

You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.

If no such element exists, then return -1.

NOTE:

Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        head = A
        l = 0
        while A != None:
            l += 1
            A = A.next
            
        mid = (l//2) + 1
        if B >= mid:
            return -1
        pos = mid - B
        
        for i in range(pos - 1):
            head = head.next
            
        return head.val
        
        
