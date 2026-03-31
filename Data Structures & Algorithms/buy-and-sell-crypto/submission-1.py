class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        prevMax = -1
        for price in prices[::-1]:
            maxDiff = max(prevMax - price, maxDiff)
            prevMax = max(price, prevMax)
        return maxDiff
