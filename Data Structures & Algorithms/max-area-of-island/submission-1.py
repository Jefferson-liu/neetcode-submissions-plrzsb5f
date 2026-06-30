from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        newGrid = []
        n = len(grid)
        m = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        newGrid.append([0 for _ in range(m + 2)])
        for i in range(n):
            newGrid.append([0, *grid[i], 0])
        newGrid.append([0 for _ in range(m + 2)])

        maxArea = 0

        seen = set()

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if newGrid[i][j] == 1 and (i, j) not in seen:
                    q = deque([(i, j)])
                    curArea = 0
                    while q:
                        row, col = q.popleft()
                        if (row, col) not in seen:
                            curArea += 1
                            for x, y in directions:
                                if (row + x, col + y) not in seen and newGrid[row + x][col + y] == 1:
                                    q.append((row + x, col + y))
                        seen.add((row, col))

                    maxArea = max(curArea, maxArea)
        return maxArea
                        

