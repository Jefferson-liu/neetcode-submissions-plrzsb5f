class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        l = 0
        r = len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                # we have to decrease so move right - 1
                r -= 1
            if curSum < target:
                # increase, move l + 1
                l += 1
            if curSum == target:
                return [l + 1, r + 1]
        return 