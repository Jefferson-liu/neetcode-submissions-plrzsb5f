class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AABBA k = 2
        # AAB len(substring) - # most frequent char 
        # AABB len(substring) - # most frequent char (A) = 2 = K
        # AABBA len(substring) - # A = 2
        # keep track of most freq char within substring
        left = 0
        right = 0
        freqs = defaultdict(int) # O(26) since only uppercase chars
        cur = 0
        maxLen = 0
        while left < len(s):
            while right < len(s):
                freqs[s[right]] += 1
                right += 1
                if freqs:
                    if right - left - max([freqs[key] for key in freqs]) > k:
                        right -= 1
                        freqs[s[right]] -= 1
                        break
            maxLen = max(right - left, maxLen) 
            freqs[s[left]] -= 1
            left += 1

        return maxLen

