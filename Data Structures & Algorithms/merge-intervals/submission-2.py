class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start
        intervals.sort(key = lambda x:x[0])
        ans = []
        curStart = intervals[0][0]
        curEnd = intervals[0][1]
        for start, end in intervals:
            if curEnd < start:
                ans.append([curStart, curEnd])
                curStart = start
                curEnd = end
            # we know start is prior so we merge
            else:
                if curEnd < end and curEnd >= start:
                    # merge
                    curEnd = end
        ans.append([curStart, curEnd])
        

                    
            
                

        return ans