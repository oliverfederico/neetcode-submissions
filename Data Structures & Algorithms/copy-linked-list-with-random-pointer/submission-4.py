"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # new nexts = old nexts, old nexts = new nexts
    # new randoms = old randoms, old randoms = new randoms
    # old: nexts -> old | randoms -> news new 
    # new: nexts -> old rand | randoms -> new rand 
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head       
        while curr:
            clone = Node(curr.val, curr.random)
            curr.random = clone
            curr = curr.next
        curr = head
        while curr:
            curr.random.random = curr.random.next.random if curr.random.next else None
            curr = curr.next
        new_head = head.random
        curr = head
        while curr:
            temp = curr.random.next
            curr.random.next = curr.next.random if curr.next else None
            curr.random = temp
            curr = curr.next
        return new_head

        

        