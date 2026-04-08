"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if a meeting starts, it would need a room, once it ends, the room is free

        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])

        startInd = 0
        endInd = 0
        res = 0
        count = 0

        while startInd < len(intervals):
            if starts[startInd] < ends[endInd]:
                count += 1
                startInd += 1
            else:
                count -= 1
                endInd += 1
            res = max(count, res)
        return res
        

