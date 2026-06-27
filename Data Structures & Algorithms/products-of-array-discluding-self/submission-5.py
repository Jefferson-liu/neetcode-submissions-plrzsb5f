class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {}
        postfix = {}
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]
        
        for i in range(len(nums) - 1, -1, - 1):
            if i == len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i + 1]
        
        ans = []
        for i in range(len(nums)):
            temp = 1
            if i - 1 in prefix:
                temp *= prefix[i - 1]
            if i + 1 in postfix:
                temp *= postfix[i + 1]
            ans.append(temp)
        return ans
