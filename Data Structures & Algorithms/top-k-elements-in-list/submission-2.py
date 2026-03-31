class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsdict = defaultdict(int)
        for num in nums:
            numsdict[num] += 1
        print(numsdict)

        sorted_list = sorted([x for x in numsdict.items()], key = lambda x:x[1], reverse = True)

        print(sorted_list)

        ans = [x[0] for x in sorted_list[:k]]
        return ans
