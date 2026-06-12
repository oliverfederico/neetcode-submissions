class MedianFinder:

    def __init__(self):
        self.left_maxh = []
        self.right_minh = []

    def addNum(self, num: int) -> None:
        if len(self.left_maxh) == len(self.right_minh):
            heapq.heappush_max(self.left_maxh, heapq.heappushpop(self.right_minh, num))
        else:
            heapq.heappush(self.right_minh, heapq.heappushpop_max(self.left_maxh, num))
        

    def findMedian(self) -> float:
        print(self.left_maxh)
        print(self.right_minh)
        if len(self.left_maxh) == len(self.right_minh):
            return (self.left_maxh[0] + self.right_minh[0])/2
        return self.left_maxh[0]

        