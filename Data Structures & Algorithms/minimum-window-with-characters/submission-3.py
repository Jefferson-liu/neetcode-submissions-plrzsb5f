class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if n < m:
            return ""
        needed = 0
        tdict = defaultdict(int)
        for char in t:
            tdict[char] += 1
            needed += 1

        sdict = defaultdict(int)

        left = 0
        right = 0
        minLen = math.inf
        minString = ""
        while right < n and left < n:
            char = s[right]
            sdict[char] += 1
            #print(sdict[char], tdict[char])
            #print(needed)
            if sdict[char] <= tdict[char] and char in tdict:
                needed = max(0, needed - 1)
            while needed == 0:
                #print(s[left:right + 1])
                #print(minLen)
                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    minString = s[left:right + 1]
                #print(s[left], sdict[s[left]])
                sdict[s[left]] = max(0, sdict[s[left]] - 1)
                needed += max(0, tdict[s[left]] - sdict[s[left]]) 
                left += 1
            right += 1
            #print(right)

        return minString

