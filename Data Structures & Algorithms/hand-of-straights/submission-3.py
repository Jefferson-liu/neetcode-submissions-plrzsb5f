from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        nums = Counter(hand)
        for num in sorted(nums):
            c = nums[num]
            if c == 0:
                continue
            for i in range(1, groupSize):
                if nums[num + i] < c:
                    return False
                nums[num + i] -= c
            nums[num] = 0

        return True