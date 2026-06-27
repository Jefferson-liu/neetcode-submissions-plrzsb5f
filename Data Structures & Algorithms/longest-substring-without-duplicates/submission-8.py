class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        maxLen = 1
        tempLen = 0
        l = 0
        r = 0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                while l < r:
                    if s[l] == s[r]:
                        l += 1
                        break
                    seen.remove(s[l])            
                    l += 1
            else:
                seen.add(s[r])
                print(seen)
                maxLen = max(maxLen, r - l + 1)
            r += 1
            
        return maxLen

        # abcabcbb
        # a, seen = a maxLen = 0-0+1
        # ab, seen = ab
        # ab, s[r] not in seen, seen = ab, maxLen = 2 - 1
        # 