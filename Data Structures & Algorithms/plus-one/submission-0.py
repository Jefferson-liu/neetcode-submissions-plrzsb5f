class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        rem = 0
        for i in range(len(digits) - 1, - 1, -1):
            if i == len(digits) - 1:
                num = digits[i] + 1
            else:
                num = digits[i] + rem

            if num >= 10:
                num = 10 % num
                rem = 1
            else:
                rem = 0
            ans.append(num)
        if rem > 0:
            ans.append(rem)
        
        return ans[::-1]