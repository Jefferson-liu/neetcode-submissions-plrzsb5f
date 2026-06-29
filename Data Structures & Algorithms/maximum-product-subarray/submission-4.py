class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1 for _ in range(n)] for _ in range(n)]
        maxProd = -1 * math.inf
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                    maxProd = max(dp[i][j], maxProd)
                else:
                    dp[i][j] = dp[i][j - 1] * nums[j]
                    maxProd = max(dp[i][j], maxProd)
        return maxProd