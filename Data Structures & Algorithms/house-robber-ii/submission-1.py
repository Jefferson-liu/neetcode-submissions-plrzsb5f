class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev, curr = 0, 0           # O(1) space
            for x in houses:
                prev, curr = curr, max(curr, prev + x)
            return curr

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))