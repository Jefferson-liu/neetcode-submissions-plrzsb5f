class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        ans = 0
        intervals.sort(key = lambda x: (-x[0], x[1])) 
        # we want to see what intervals overlap the MOST intervals
        # for example, we store minStart and maxStart
        #print(intervals)
        ans = 0
        prevStart, prevEnd = intervals[0]
        for start, end in intervals:
            if prevStart < end and prevEnd > start:
                # overlapping
                #print(prevStart, prevEnd, start, end)
                ans += 1
            else:
                prevStart = start
                prevEnd = end
        return ans - 1
