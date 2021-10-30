'''Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def reverse(head):
    prev = None
    curr = head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    return prev
    
def compare(A, B):
    head1 = A
    head2 = B
    while head1 != None and head2 != None:
        if head1.val != head2.val:
            return 0
        head1 = head1.next
        head2 = head2.next
        
    return 1

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        count = 0
        mid = A
        head = A
        prev = A
        while head != None:
            if count%2 == 1:
                prev = mid
                mid = mid.next
            count += 1
            head = head.next
            
        if count%2 == 1:
            mid = mid.next
            
        firstHalf = A
        prev.next = None
        secondHalf = mid
        secondHalf = reverse(secondHalf)
        return compare(firstHalf, secondHalf)
        
