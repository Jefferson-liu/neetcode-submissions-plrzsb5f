class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        maxSum = -1 * math.inf
        curSum = 0
        while right < len(nums):
            if curSum + nums[right] < 0:
                left = right
                curSum = nums[left]
            else:
                curSum += nums[right]
                if nums[left] < 0:
                    curSum -= nums[left]
                    left += 1
                    
            right += 1
            maxSum = max(maxSum, curSum)
        
        return maxSum