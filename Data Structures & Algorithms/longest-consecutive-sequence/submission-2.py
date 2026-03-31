class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for num in nums:
            numset.add(num)
        maxlen = 0
        
        for num in nums:
            if num - 1 not in numset:
                temp = 1
                while num + temp in numset:
                    temp += 1
                maxlen = max(temp, maxlen)
        return maxlen
                    
