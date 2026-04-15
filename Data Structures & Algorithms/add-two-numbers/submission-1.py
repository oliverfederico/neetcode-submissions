# Definition for singly-linked list.
# class ListNode:
from types import resolve_bases
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = l1
        carry = 0
        while l1:
            l1.val += carry
            carry = 0
            if l2:
                l1.val += l2.val
                if not l1.next:
                    l1.next = l2.next
                    l2.next = None
                l2 = l2.next
            if l1.val > 9:
                carry = 1
                l1.val = l1.val % 10
            if not l1.next and carry:
                l1.next = ListNode(1)
                break
            l1 = l1.next
        return result            
                
            