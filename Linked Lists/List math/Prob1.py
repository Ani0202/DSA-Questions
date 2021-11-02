'''You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain 
a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        node = ListNode(None)
        head = node
        carry = 0
        while A != None or B != None:
            if A != None:
                a = A.val
                A = A.next
            else:
                a = 0
                
            if B != None:
                b = B.val
                B = B.next
            else:
                b = 0
            
            n = (a + b + carry) % 10
            head.next = ListNode(n)
            carry = (a + b + carry)//10
            head = head.next
            
        if carry:
            head.next = ListNode(carry)
                
        return node.next
