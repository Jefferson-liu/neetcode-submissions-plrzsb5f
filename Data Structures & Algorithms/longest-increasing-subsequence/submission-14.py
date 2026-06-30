from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @lru_cache(maxsize = None)
        def dfs(prev, ind):
            if ind == len(nums):
                return 0
            LIS = dfs(prev, ind + 1)
            if nums[prev] < nums[ind] or prev == -1:
                LIS = max(LIS, 1 + dfs(ind, ind + 1))
            return LIS
            
        
        return dfs(-1, 0)
