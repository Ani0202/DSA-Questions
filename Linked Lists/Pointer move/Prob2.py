'''Given a linked list A , reverse the order of all nodes at even positions.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        head = A
        c = 0
        l = list()
        while A != None:
            if c == 1:
                l.append(A.val)
                
            A = A.next
            c = (c+1)%2
            
        l.reverse()
        head2 = head
        i = 0
        c = 0
        while head != None:
            if c == 1:
                head.val = l[i]
                i += 1
                
            head = head.next
            c = (c+1)%2
            
        return head2
