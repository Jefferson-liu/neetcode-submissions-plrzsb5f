class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        cur = []
        ans = []
        def rec(ind):
            if ind == n:
                return
            # we take one or we can skip one
            cur.append(nums[ind])
            ans.append(cur[::])
            rec(ind + 1)
            cur.pop()
            rec(ind + 1)
        
        rec(0)
        ans.append([])
        return ans
