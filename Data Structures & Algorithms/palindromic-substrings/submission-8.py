class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)] # such that s[i][j] tracks whether or not s[i:j] is a palindrome
        counter = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    #print(i, j)
                    dp[i][j] = True
                    counter += 1
        return counter
        