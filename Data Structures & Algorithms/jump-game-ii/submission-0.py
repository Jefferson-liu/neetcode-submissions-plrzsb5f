class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf for _ in range(n)]
        dp[0] = 0
        for i, num in enumerate(nums):
            for k in range(1, num + 1):
                if k + i < n:
                    dp[k + i] = min(dp[k + i], dp[i] + 1)
        #print(dp)
        return dp[-1]
