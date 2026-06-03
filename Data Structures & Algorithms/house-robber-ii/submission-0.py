class Solution:
    def rob(self, nums: List[int]) -> int:
        # try to do prev solution
        dp = []
        for i in range(len(nums)):
            dp.append([0,0])
        if len(nums) <= 3:
            return max(nums)
        # [max w robbed first, max w not robbed first]
        dp[0] = [nums[0],0]
        dp[1] = [nums[0],nums[1]]
        ans = 0
        for idx, num in enumerate(nums):
            # we either can steal or not
            if idx > 1 and idx < len(nums) - 1:
                dp[idx][0] = max(dp[idx-2][0] + nums[idx], dp[idx - 1][0])
                dp[idx][1] = max(dp[idx-2][1] + nums[idx], dp[idx - 1][1])      
            if idx == len(nums) - 1:
                dp[idx][0] = 0
                dp[idx][1] = max(dp[idx-2][1] + nums[idx], dp[idx - 1][1])
            ans = max(ans, max(dp[idx]))
        
        return ans
