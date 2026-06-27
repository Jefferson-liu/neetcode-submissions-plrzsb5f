from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of max character counts
        if len(s) <= 1:
            return 1
        counts = [0 for _ in range(26)]
        l = 0
        r = 0
        maxLen = 0
        while r < len(s):
            counts[ord(s[r]) - ord("A")] += 1
            while r - l - max(counts) + 1 > k:
                counts[ord(s[l]) - ord("A")] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            
            r += 1
            
        return maxLen

                
            