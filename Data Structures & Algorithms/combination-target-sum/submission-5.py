class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(cur, curSum, comb):
            if cur >= len(nums):
                return
            new = comb[::]
            new.append(nums[cur])

            if curSum + nums[cur] == target:
                ans.append(new)
            if curSum + nums[cur] < target:
                # we choose cur
                dfs(cur, curSum + nums[cur], new)
                new.pop()
            else:
                return
            dfs(cur + 1, curSum, new)
        
        dfs(0, 0, [])
        return ans
            
