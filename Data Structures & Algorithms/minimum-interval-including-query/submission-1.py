from collections import defaultdict
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:


        data = {}

        for start, end in intervals:
            l = end - start + 1
            for i in range(start, end + 1):
                if i in data:
                    if data[i] > l:
                        data[i] = l
                else:
                    data[i] = l
        
        ans = []
        for query in queries:
            if query in data:
                ans.append(data[query])
            else:
                ans.append(-1)
        return ans