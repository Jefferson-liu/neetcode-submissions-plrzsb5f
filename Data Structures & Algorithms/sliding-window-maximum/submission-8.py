import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # left, right 
        # store a heap with indices as second value
        if k == 1:
            return nums
        left = 0
        target = []
        ans = []
        for i in range(len(nums)):
            heapq.heappush_max(target, (nums[i], i))
            if i - left + 1 == k:
                #print(target)
                #print(cur)
                while target[0][1] < left or target[0][1] > i:
                    heapq.heappop_max(target)
                ans.append(target[0][0])
                left += 1

        return ans
            
            
            