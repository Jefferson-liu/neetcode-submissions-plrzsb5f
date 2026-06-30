from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        seen = set()

        n = len(grid)
        m = len(grid[0])
        newGrid = [["0" for _ in range(m + 2)]]

        for i in range(n):
            temp = ["0"]
            temp.extend(grid[i])
            temp.append("0")
            newGrid.append(temp)
        
        newGrid.append(["0" for _ in range(m + 2)])
        print(newGrid)


        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        islands = 0
        for i in range(1,n + 1):
            for j in range(1, m + 1):
                if (i, j) not in seen:
                    if newGrid[i][j] == "1":
                        q = deque([(i, j)])
                        while q:
                            row, col = q.popleft()
                            if newGrid[row][col] == "1":
                                seen.add((row,col))
                                for x, y in directions:
                                    if (row + x, col + y) not in seen:
                                        q.append((row + x, col + y))
                        islands += 1

        print(seen)
        return islands

                        