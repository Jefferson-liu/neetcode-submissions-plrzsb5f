class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n)]
        # how many ways to reach stage
        if n <= 2:
            return n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            # choose to climb one step or climb two steps
            dp[i] += dp[i - 1] # that is one choice
            # climb two steps
            # the second step is i + 2 so we add one to the next one
            dp[i] += dp[i - 2]
        print(dp)
        return dp[-1]