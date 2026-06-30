from collections import defaultdict
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # segment tree
        # define a data class where a node contains start, end
        # HUGE PREFIX DATACLASS

        data = {}

        for start, end in intervals:
            l = end - start + 1
            for i in range(start, end + 1):
                if i in data:
                    if data[i][0] > l:
                        data[i] = [l, start, end]
                else:
                    data[i] = [l, start, end]
        
        ans = []
        for query in queries:
            if query in data:
                ans.append(data[query][0])
            else:
                ans.append(-1)
        return ans