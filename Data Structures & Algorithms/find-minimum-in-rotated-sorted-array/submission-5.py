class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min value is either the first value or the value before it is greater than it
        left = 0
        n = len(nums)
        right = n - 1
        minVal = math.inf
        while left <= right:
            mid = (right + left) // 2
            # if nums[left] > nums[mid], we know that minimum is between indexes left and mid
            # if nums[right] < nums[mid], we know min between right and mid
            # if nums[left] < nums[mid] AND nums[right] > nums[mid], we know that its a regular sorted array, min at nums[left]
            if nums[left] > nums[mid]:
                minVal = min(nums[mid], minVal)
                right = mid - 1
            elif nums[right] < nums[mid]:
                minVal = min(nums[mid], minVal)
                left = mid + 1
            elif nums[left] < nums[mid] and nums[mid] < nums[right]:
                minVal = min(nums[left], minVal)
                print(left, right)
                return minVal
            else:
                print(left, right)
                print(mid)
                return min(minVal, nums[mid])
        print(mid)
        return min(minVal, nums[0])