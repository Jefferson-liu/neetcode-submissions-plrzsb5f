class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp problem
        dp = [0] * len(nums)
        print(dp)
        if len(nums) <= 2:
            return max(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        # we can rob either this house or the next house
        for idx, num in enumerate(nums):
            # can rob this house if we did not rob the previous house
            # add the dp[idx-2]
            if idx >= 2:
                dp[idx] = max(dp[idx - 2] + nums[idx], dp[idx - 1]) # rob cur house, add max prev val
        print(dp)
        return max(dp)

            
            