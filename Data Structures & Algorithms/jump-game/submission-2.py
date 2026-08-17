class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if farthest >= i:
                farthest = max(nums[i] + i, farthest)
        
        return farthest >= len(nums) - 1

            
