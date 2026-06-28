class Solution:
    def findMin(self, nums: List[int]) -> int:
        # assume its sorted based on rotation?

        l = 0
        r = len(nums)- 1
        minVal = math.inf
        while l <= r:
            mid = (r + l) // 2
            minVal = min(nums[mid], minVal)
            minVal = min(minVal, nums[r])
            if nums[mid] > nums[l] and nums[r] < nums[l]:
                # rotated
                l = mid + 1
            else:
                # nums[l] > nums[mid]
                r = mid - 1
        return minVal