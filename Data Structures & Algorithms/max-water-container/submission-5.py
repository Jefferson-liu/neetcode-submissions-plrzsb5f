class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        maxA = 0
        if len(heights) <= 1:
            return 0
        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            curA = min(heights[l], heights[r]) * width
            maxA = max(maxA, curA)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxA