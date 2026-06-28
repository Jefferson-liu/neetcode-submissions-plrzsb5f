from collections import defaultdict
class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        counts = dict()
        needed = 0
        for char in t:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
            needed += 1
        minLen = len(s) + 1
        minString = ""
        l = 0
        r = 0
        tempCounts = defaultdict(int)
        while r < len(s) and l <= r:
            if s[r] in counts:
                if tempCounts[s[r]] < counts[s[r]]:
                    needed -= 1
                tempCounts[s[r]] += 1
            while needed == 0:
                if minLen > r - l + 1:
                    minString = s[l:r + 1]
                    minLen = r - l + 1
                if tempCounts[s[l]] > 0:
                        tempCounts[s[l]] -= 1
                if s[l] in counts:
                    if counts[s[l]] > tempCounts[s[l]]:
                        needed += 1
                l += 1
            r += 1
        return minString