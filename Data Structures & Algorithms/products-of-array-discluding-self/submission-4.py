from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = defaultdict(int)
        postfixes = defaultdict(int)
        n = len(nums)
        for i in range(n):
            if i == 0:
                prefixes[i] = nums[i]
            else:
                prefixes[i] = prefixes[i-1] * nums[i]
        for i in range(n-1,-1,-1):
            if i == n-1:
                postfixes[i] = nums[i]
            else:
                postfixes[i] = postfixes[i+1] * nums[i]
        ans = []
        for i in range(n):
            if i == 0:
                ans.append(postfixes[i + 1])
            elif i == n - 1:
                ans.append(prefixes[n - 2])
            else:
                ans.append(prefixes[i - 1] * postfixes[i + 1])
        #print(ans)
        return ans