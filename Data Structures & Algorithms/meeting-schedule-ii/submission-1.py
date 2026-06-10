"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: (x.start, -x.end))
        max_rooms = 0
        end_times = []

        for interval in intervals:
            if end_times and interval.start >= heapq.nsmallest(1, end_times)[0]:
                heapq.heappushpop(end_times, interval.end)
            else:
                heapq.heappush(end_times, interval.end)
                # max_rooms = max(max_rooms, len(end_times))



            
        return len(end_times) 