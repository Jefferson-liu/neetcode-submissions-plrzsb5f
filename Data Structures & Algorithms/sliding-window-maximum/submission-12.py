import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # put in a maxheap until index is within the window
        
        heap = []
        for i in range(k):
            heapq.heappush_max(heap, (nums[i], i))
        ans = []
        for i in range(len(nums) - k + 1):
            while heap[0][1] < i:
                heapq.heappop_max(heap)
            ans.append(heap[0][0])
            if i + k < len(nums):
                heapq.heappush_max(heap, (nums[i + k], i + k))
        return ans

