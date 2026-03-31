class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = set()
        for i, num in enumerate(nums):
            if num == 0:
                zeroes.add(i)
            else:
                prod *= num
        
        ans = []
        for i, num in enumerate(nums):
            if len(zeroes) > 1:
                ans.append(0)
            elif num == 0:
                ans.append(prod)
            else:
                if len(zeroes) > 0:
                    ans.append(0)
                else:
                    ans.append(prod//num)
        return ans

            

