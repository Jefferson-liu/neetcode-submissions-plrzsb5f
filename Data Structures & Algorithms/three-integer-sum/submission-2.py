class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum2 = defaultdict(list)

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum2[nums[i]+nums[j]].append([i,j])
        
        ans = []
        seen = set()
        for i in range(len(nums)):
            if nums[i] * -1 in sum2:
                for a,b in sum2[nums[i] * -1]:
                    if i < a:
                        if tuple(sorted([nums[i], nums[a], nums[b]])) not in seen:
                            ans.append(sorted([nums[i], nums[a], nums[b]]))
                            seen.add(tuple(sorted([nums[i], nums[a], nums[b]])))
        return ans
