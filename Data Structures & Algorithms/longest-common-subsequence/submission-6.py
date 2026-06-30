class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        long = text1
        short = text2
        if len(text1) < len(text2):
            long, short = text2, text1

        n = len(long)
        m = len(short)
        dp = [0 for _ in range(m + 1)]

        # we are checking longest subsequence of short that is also in long
        # we track i, j, x, y
        # we know x is less than i
        # so lets say text1[i] = text2[j]
        # then for each of s[x] == s[y], where we are incrementing

        for i in range(n - 1, - 1, - 1):
            prev = 0
            for j in range(m - 1, - 1, - 1):
                temp = dp[j]
                if long[i] == short[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = temp
        print(dp)
        return dp[0]
