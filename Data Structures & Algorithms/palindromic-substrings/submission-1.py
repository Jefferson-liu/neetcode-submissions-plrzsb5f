class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        #count how many palindromes so dp[i,j] is a palindrome from those points
        n = len(s)
        if len(s) <= 1:
            return 1
        ans = 0
        

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans += 1
        #print(dp)
        
        
        return ans
        
                