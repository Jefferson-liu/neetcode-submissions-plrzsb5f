class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        nextVal = sum([int(c) * int(c) for c in str(n)])
        while nextVal not in seen:
            seen.add(nextVal)
            if nextVal == 1:
                return True
            nextVal = sum([int(c) * int(c) for c in str(nextVal)])
            
        
        return False
