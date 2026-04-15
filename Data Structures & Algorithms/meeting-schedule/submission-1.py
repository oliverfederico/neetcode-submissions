"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # sort by end time? and look for overlap with previous meeting, if start of curr < end of prev
    # nlog to sort and then n to validate, n space. 

    # will input always be sorted by start time
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        prev = -1
        for interval in intervals:
            if interval.start < prev:
                return False
            prev = interval.end
        return True
