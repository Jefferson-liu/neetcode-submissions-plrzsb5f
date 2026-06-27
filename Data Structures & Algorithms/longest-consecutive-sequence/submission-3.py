class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longestLen = 0
        for num in setNums:
            if num - 1 not in setNums:
                tempNum = num
                tempLen = 0
                while tempNum in setNums:
                    tempNum += 1
                    tempLen += 1
                longestLen = max(tempLen, longestLen)
        return longestLen