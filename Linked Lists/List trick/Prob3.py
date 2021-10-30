'''Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question. '''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        head = A
        tail = None
        for i in range(B-1):
            tail = A
            A = A.next
        prev = None
        curr = A
        for i in range(C - B + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        A.next = curr
        if tail == None:
            return prev
        tail.next = prev
        return head
        
            