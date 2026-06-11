# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    # we know the smallest element of each list,  priority queue  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i))
        res = ListNode()
        curr = res
        while heap:
            _, i = heapq.heappop(heap)
            while lists[i] and (not heap or lists[i].val <= heap[0][0]):
                curr.next = lists[i]
                curr = curr.next
                lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return res.next