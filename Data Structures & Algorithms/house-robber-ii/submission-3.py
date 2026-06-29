class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(0,0) for _ in range(n)] 
        # we need to know if we robbed the first house, so dp[i][0] is max val given robbed first house, 
        # dp[i][1] is max val given NOT robbed prev house
        # just do two dps
        dp[0] = (nums[0], 0)
        for i in range(n - 1):
            dp[i] = (max(dp[i-1][1] + nums[i], dp[i-1][0]), dp[i-1][0])
        dp[-1] = dp[n-2]
        dp2 = [(0,0) for _ in range(n)]
        if n > 1:
            dp2[1] = (nums[1], 0)
            for i in range(1, n):
                dp2[i] = (max(dp2[i-1][1] + nums[i], dp2[i-1][0]), dp2[i-1][0])
        
        return max(max(dp[-1]), max(dp2[-1]))
