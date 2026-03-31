class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we want to maximize distance left height and right height
        maxWater = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            dist = right - left
            water = dist * min(heights[left], heights[right])
            maxWater = max(water, maxWater)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxWater
