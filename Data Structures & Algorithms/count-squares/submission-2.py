from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.xPoints = defaultdict(set)
        self.yPoints = defaultdict(set)
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x,y)] += 1
        
        self.yPoints[y].add((x,y))
        
        self.xPoints[x].add((x,y))

    def count(self, point: List[int]) -> int:
        x, y = point
        
        ans = 0
        
        for a, b in self.xPoints[x]:
            for c, d in self.yPoints[y]:
                if b != y and c != x:
                    ans += (self.points[(a,b)] * self.points[(c,d)] * self.points[(c, b)])
        return ans
                    
        
