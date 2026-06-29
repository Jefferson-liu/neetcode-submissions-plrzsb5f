class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if amount == 0:
            return 0
        if dp[amount] < math.inf:
            return dp[amount]
        return -1