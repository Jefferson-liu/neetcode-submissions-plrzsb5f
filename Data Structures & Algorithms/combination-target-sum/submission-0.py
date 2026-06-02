class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, curList, total):
            if total == target:
                ans.append(curList[:])   # snapshot
                return
            if total > target or i >= len(nums):
                return
            # choice 1: use nums[i] again, stay at i
            curList.append(nums[i])
            backtrack(i, curList, total + nums[i])
            curList.pop()
            # choice 2: skip nums[i] forever, move to i+1
            backtrack(i + 1, curList, total)
        backtrack(0, [], 0)
        return ans