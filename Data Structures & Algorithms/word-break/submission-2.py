class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we can just store if a substring can be broken down
        n = len(s)
        dp = [False] * (n + 1)
        if n < min([len(word) for word in wordDict]):
            return False
        
        for word in wordDict:
            if len(word) <= n:
                if s[:len(word)] == word:
                    dp[len(word)] = True
        
        for i in range(n + 1):
            for word in wordDict:
                if i - len(word) > 0:
                    #print(s[i-len(word):])
                    #print(word)
                    #print(s[i-len(word):].startswith(word))
                    if dp[i-len(word)] and s[i-len(word):].startswith(word):
                        dp[i] = True
        #print(dp)
        return dp[-1]