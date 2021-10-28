'''Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.

NOTE:

Try to do it in constant space.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        head = A
        zeroes = 0
        ones = 0
        while head != None:
            if head.val == 0:
                zeroes += 1
            else:
                ones += 1
            head = head.next
            
        head = A
        while head != None:
            if zeroes:
                head.val = 0
                zeroes -= 1
            else:
                head.val = 1
            head = head.next
            
        return A
