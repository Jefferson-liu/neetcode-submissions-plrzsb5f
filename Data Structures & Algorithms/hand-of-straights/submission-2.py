from collections import defaultdict, deque
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        nums = defaultdict(int)
        for num in hand:
            nums[num] += 1
        # card values are consecutively increasing by 1, lowest number needs to be in, highest number needs to be in , then do recursion?
        # sorted set
        hs = deque(sorted(list(set(hand))))
        while hs:
            pops = 0
            for i in range(groupSize):
                if i >= len(hs):
                    return False
                if nums[hs[i]] == 0 or i > 0 and hs[i - 1] + 1 != hs[i]:
                    return False
                nums[hs[i]] -= 1
                if nums[hs[i]] == 0:
                    
                    pops += 1
            for i in range(pops):
                hs.popleft()
                
        return True