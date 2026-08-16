class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True
        for i in range(len(nums)):
            if dp[i]:
                for k in range(nums[i] + 1):
                    if i + k < len(dp):
                        dp[i + k] = True
        
        return dp[-1]

            
