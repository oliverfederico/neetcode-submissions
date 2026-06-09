class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # build array from min end to max end
        # track 
        max_end = max(interval[1] for interval in intervals)
        min_end = min(interval[1] for interval in intervals)
        starts = [float('-inf')] * (max_end - min_end + 1)
        for start, end in intervals:
            starts[end - min_end] = max(starts[end - min_end], start)
        
        i = 0
        kept_intervals = 0
        last_valid_end = float('-inf')
        while i < len(starts):
            max_start = starts[i]
            if max_start >= last_valid_end:
                kept_intervals += 1
                last_valid_end = i + min_end
            i+=1
        
        return len(intervals) - kept_intervals

        