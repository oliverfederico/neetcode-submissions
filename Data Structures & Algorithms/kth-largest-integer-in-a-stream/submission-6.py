class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        if len(self.heap) < k:
            heapq.heappush(self.heap, -1001)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappushpop(self.heap, val)
        return self.heap[0]
