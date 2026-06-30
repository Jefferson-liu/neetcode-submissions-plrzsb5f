class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(prev, ind):
            if ind == len(nums):
                return 0
            if (prev, ind) in memo:
                return memo[(prev, ind)]

            memo[(prev, ind)] = dfs(prev, ind + 1)
            
            if nums[prev] < nums[ind] or prev == -1:
                memo[(prev, ind)] = max(memo[(prev, ind)], 1 + dfs(ind, ind + 1))
            
            memo[(prev, ind + 1)] = memo[(prev, ind)]
            return memo[(prev, ind)]
            
        
        return dfs(-1, 0)
