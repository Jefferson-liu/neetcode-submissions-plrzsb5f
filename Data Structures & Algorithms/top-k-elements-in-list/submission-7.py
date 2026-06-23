from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums) + 1)] 
        counts = dict(Counter(nums))
        for num in counts:
            print(num)
            print(counts[num])
            arr[counts[num]].append(num)
        ans = []
        cur = len(arr) - 1
        count = 0
        while count < k and cur >= 0:
            if len(arr[cur]) > 0:
                for i in arr[cur]:
                    if count < k:
                        ans.append(i)
                        count += 1
            cur -= 1
        return ans
        
                

