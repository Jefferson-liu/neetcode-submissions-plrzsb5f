class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer slices
        water = 0
        for i in range(1, len(height) - 1):
            l = i - 1
            r = i + 1
            maxL = 0
            maxR = 0
            while l >= 0:
                maxL = max(height[l], maxL)
                l -= 1
            while r < len(height):
                maxR = max(height[r], maxR)
                r += 1
            #print(i, maxR, maxL, height[i])
            water += max(min(maxL, maxR) - height[i], 0)
        return water