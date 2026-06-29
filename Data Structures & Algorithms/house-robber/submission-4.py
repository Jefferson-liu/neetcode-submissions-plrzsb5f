class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(0,0) for _ in range(n)] # either we are robbing the current house or skipping the current house
        # dp[i][0] means max value given we rob current house, dp[i][1] means max value given we skip current house
        dp[0] = (nums[0], 0)
        for i in range(1,n):
            dp[i] = (max(dp[i-1][1] + nums[i], dp[i-1][0]), dp[i-1][0]) 
            # max value of skipped prev house and rob this house or skipped house, or we skip current house 
        return max(dp[-1])
