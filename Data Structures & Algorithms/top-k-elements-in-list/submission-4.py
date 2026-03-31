class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsdict = defaultdict(int)
        for num in nums:
            numsdict[num] += 1
        print(numsdict)

        ans = [[] for _ in range(len(nums))]
        print(ans)


        for num in numsdict:
            print(numsdict[num])
            ans[numsdict[num] - 1].append(num)
        
        freqs = []
        for a in ans:
            if len(a) > 0:
                freqs.extend(a)
        print(freqs)

        return freqs[::-1][:k]




