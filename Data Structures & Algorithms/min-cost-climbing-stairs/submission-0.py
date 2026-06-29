class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(len(cost) + 1)]

        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n + 1):
            # we choose to either go to the next floor or the next next floor
            dp[i] = min(dp[i-1], dp[i-2])
            if i < n:
                dp[i] += cost[i]
        return dp[-1]
        