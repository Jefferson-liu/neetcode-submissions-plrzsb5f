class Solution:
    def findMin(self, nums: List[int]) -> int:
        # assume its sorted based on rotation?

        l = 0
        r = len(nums)- 1
        while l < r:
            mid = (r + l) // 2
            
            if nums[mid] > nums[r]:
                # rotated
                l = mid + 1
            else:
                # nums[l] > nums[mid]
                r = mid
        return nums[l]