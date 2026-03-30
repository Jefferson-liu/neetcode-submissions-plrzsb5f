class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)

        for i, num in enumerate(nums):
            dic[num].append(i)

            if (target - num) in dic:
                if target - num != num:
                    return [dic[target - num][0], i]
                else:
                    if target - num == num:
                        if len(dic[num]) > 1:
                            return [dic[num][0], dic[num][1]]
        
        