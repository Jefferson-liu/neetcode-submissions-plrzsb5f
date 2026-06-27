class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 2000 elements in that array, we have to return k most frequent elements in the array
        # can we do a bucket sort?
        # whenever we see a k value, increment the value at k, then its only O(n) to parse through array once, then O(2000) to sort it one time which is constant
        buckets = [[i, 0] for i in range(2000)]
        for num in nums:
            buckets[num + 1000][1] += 1
        
        buckets.sort(key = lambda x:x[1], reverse = True)
        #print(buckets[:k])
        return [x[0]-1000 for x in buckets[:k]]