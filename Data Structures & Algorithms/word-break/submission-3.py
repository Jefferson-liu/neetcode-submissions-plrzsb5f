class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(n):
            cur = s[i:]
            if dp[i]:
                for word in wordDict:
                    if cur.startswith(word):
                        dp[i + len(word)] = True
        return dp[-1]
                    
