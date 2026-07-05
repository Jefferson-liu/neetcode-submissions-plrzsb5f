class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        def dfs(curSum, curNums, i):
            if curSum == target:
                ans.append(curNums[:])
                return
            if i >= n or curSum > target:
                return
            
            # we can walk through nums and check if we want this or not
            curNums.append(nums[i])
            dfs(curSum + nums[i], curNums, i)
            curNums.pop()
            dfs(curSum, curNums, i + 1)
        
        dfs(0, [], 0)
        return ans
