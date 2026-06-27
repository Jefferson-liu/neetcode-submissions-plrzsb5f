class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer slices
        water = 0
        maxL = 0
        maxR = 0
        r = 1
        maxRw = 0
        while r < len(height):
            if height[r] > maxRw:
                maxR = r
                maxRw = height[r]
            r += 1
        
        #print(maxR)
        for i in range(1, len(height) - 1):
            if height[i] > height[maxL]:
                maxL = i
            if i == maxR:
                maxL = i
                r = i + 1
                maxRw = 0
                while r < len(height):
                    if height[r] > maxRw:
                        maxR = r
                        maxRw = height[r]
                    r += 1
            
            #print(i, maxR, maxL, height[i])

            water += max(min(height[maxL], height[maxR]) - height[i], 0)
        return water