class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can keep a sorted list of most frequent elements of the array, would be O(n^2)
        
        numdict = defaultdict(int)
        for num in nums:
            numdict[num] += 1
        ans = []
        for _ in range(len(nums)):
            ans.append([])
        
        for num in numdict:
            ans[numdict[num] - 1].append(num)
        a = []
        print(ans)
        for ls in ans:
            if len(ls) > 0:
                a.extend(ls)
        print(a)
        return a[::-1][:k]

