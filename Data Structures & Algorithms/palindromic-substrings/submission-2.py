class Solution:
    def countSubstrings(self, s: str) -> str:
        res = 0

        def expand(left, right):
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            return res  # step back to the valid range

        for i in range(len(s)):
            res += expand(i,i)
            res += expand(i,i+1)
        return res