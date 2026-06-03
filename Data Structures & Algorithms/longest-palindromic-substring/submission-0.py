class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]   # step back to the valid range

        best = ""
        for i in range(len(s)):
            odd  = expand(i, i)        # center on one char
            even = expand(i, i + 1)    # center between two chars
            best = max(best, odd, even, key=len)
        return best