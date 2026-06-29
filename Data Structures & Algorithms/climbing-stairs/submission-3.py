class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        # how many ways to reach stage
        if n <= 2:
            return n
        dp[0] = 1
        dp[1] = 1
        for i in range(n):
            # choose to climb one step or climb two steps
            dp[i + 1] += dp[i] # that is one choice
            # climb two steps
            # the second step is i + 2 so we add one to the next one
            if i + 2 < n:
                dp[i + 2] += dp[i]
        print(dp)
        return dp[-1]