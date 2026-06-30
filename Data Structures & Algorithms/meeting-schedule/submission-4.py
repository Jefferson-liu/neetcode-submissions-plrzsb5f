"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        if len(intervals) == 0:
            return True
        prevEnd = intervals[0].end
        prevStart = intervals[0].start
        print([(x.start, x.end) for x in intervals])
        for x in intervals[1:]:
            start = x.start
            end = x.end
            if prevEnd > start:
                return False
            prevEnd = end
            prevStart = start
        return True
