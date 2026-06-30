class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n + 1)]
        # the base case is that the longest subsequence is 1
        # lets use x as the start of the longest subsequence
        # i.e dp[x] = LIS starting at i
        # build up from the back
        # iterate from the front
        # for example, take nums[i] = 7, nums[j] = 1
        # we let i > j for everything so if i > j, then we know that the subsequence starting at j can either 
        # include the subsequence starting at i or not include the subsequence starting at i
        # n = [1,2, 4, 3],
        # i = 3, j = 0
        # n[i] > n[j] so dp[j] = max(1 + dp[i], dp[j]), dp = [2,1,1,1]
        # i = 3, j = 1
        # same thing, dp = [2,2,1,1]
        # i = 3, j = 2
        # dp = [2,2,1,1] since 4 > 3
        # i = 2, j = 0
        # dp = [2,2,1,1] since dp[i] == 1 and dp[j] == 2
        # j = 1, same thing
        # i = 1, j = 0
        # dp = [3,2,1,1], 
        # logic is that we build out LIS from the back, so as we go from the front, we can add 1 to the LIS starting at the back
        # OR we don't add 1 to the LIS starting from the back if our current length is already longer\
        maxVal = 1
        for i in range(n - 1, -1, -1):
            for j in range(i): # j is less than i
                if nums[i] > nums[j]:
                    dp[j] = max(1 + dp[i], dp[j])
                    maxVal = max(maxVal, dp[j])
        return maxVal
        