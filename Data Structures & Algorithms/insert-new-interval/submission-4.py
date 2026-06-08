import bisect
class Solution:
    # idx = bisectleft on newstart, if idx - 1 end >= newstart, we merge from idx - 1. 
    # we bisectleft on newend (j) and merge i-j intervals    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        
        # Step 1: Skip intervals that end before the newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            i += 1
            
        start_index = i
        
        # Step 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        # Step 3: Replace the merged overlapping chunk with the updated newInterval
        # This is done in-place without allocating a new output array
        intervals[start_index:i] = [newInterval]
        
        return intervals