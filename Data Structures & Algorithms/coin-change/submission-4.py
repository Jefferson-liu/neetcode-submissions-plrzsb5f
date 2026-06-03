class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        # fewest number of coins to make up each amount, we want to see fewest number of coins for each value up to amount and then see if its possible
        if amount == 0:
            return 0
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(amount + 1):
            for coin in coins:
                if i - coin > 0:
                    if dp[i-coin] < math.inf:
                        dp[i] = min(dp[i], dp[i-coin] + 1)
        print(dp)
        if dp[amount] < math.inf:       
            return dp[amount]
        return -1

            
