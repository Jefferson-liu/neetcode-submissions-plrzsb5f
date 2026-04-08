class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals already sorted by start
        # parse through intervals until some interval start > newInterval beginning, 
        # if newInterval end is greater than curinterval end, we look at start of the next, if our end is greater than start, we look at start of the next one
        # until the starts are no longer greater than end of curInterval, then check prev End, and the new interval will be at curStart and tempEnd, check 
        # [[0,1] [2,3]] [0,3]
        #  [[0,1] [0,3] [2,3]]
        newStart, newEnd = newInterval
        result =[]
        n = len(intervals)
        i = 0
        if n == 0:
            return [newInterval]

        while i < n and intervals[i][1] < newStart:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newEnd:
            newStart = min(intervals[i][0], newStart)
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        result.append([newStart, newEnd])
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
                    
                

            

                
