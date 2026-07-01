from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs

        minMin = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        board = []
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        board.append([[0, 0] for _ in range(m + 2)])
        for i in range(n):
            for x in grid[i]:
                if x == 1:
                    fresh += 1
            board.append([[0, 0], *[[0, x] for x in grid[i]], [0, 0]])
        board.append([[0, 0] for _ in range(m + 2)])

        rotted = deque([])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if board[i][j][1] == 2:
                    rotted.append((0, i, j))
        
        # locations of rotted fruits
        prevTime = 0
        
        while rotted:
            time, row, col = rotted.popleft()
            fresh -= 1
            prevTime = time
            for x, y in directions:
                if board[row + x][col + y][1] == 1:
                    board[row + x][col + y] = [time + 1, 2]
                    rotted.append((time + 1, row + x, col + y))
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if board[i][j][1] == 1:
                    return -1
        return prevTime
            



