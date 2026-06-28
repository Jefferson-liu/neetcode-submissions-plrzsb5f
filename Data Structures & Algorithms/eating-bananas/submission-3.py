class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def ub(rate):
            total = 0
            for pile in piles:
                time, rem = divmod(pile, rate)
                if rem > 0:
                    time += 1
                total += time
            return total

        l = 1
        r = max(piles)
        lowest = r
        while l <= r:
            mid = (l + r) // 2
            if ub(mid) <= h:
                lowest = min(mid, lowest)
                r = mid - 1
            elif ub(mid) > h:
                l = mid + 1


        return lowest
        