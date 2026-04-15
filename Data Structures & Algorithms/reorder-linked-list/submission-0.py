# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # first half zipped with reverse of second half
    def reorderList(self, head: Optional[ListNode]) -> None:
        #reverse second half in place
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        succ = slow.next
        slow.next = None
        while succ:
            succ.next, succ, prev = prev, succ.next, succ
        main = head
        while prev:
            main.next, prev.next, main, prev = prev, main.next, main.next, prev.next
            


