from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        n = len(board)
        m = len(board[0])
        def isStart(x, y, ind, seen):
            
            if board[x][y] != word[ind]:
                return False
            if ind == len(word) - 1:
                return True
            new = seen.copy()
            new.add((x, y))
                
            for dx, dy in directions:
                if dx + x < n and dx + x >= 0 and dy + y < m and dy + y >= 0 and (x + dx, y + dy) not in new:
                    if board[x + dx][y + dy] == word[ind + 1]:
                        if isStart(x + dx, y + dy, ind + 1, new):
                            return True
            return False

        for i in range(n):
            for j in range(m):
                if isStart(i, j, 0, set()):
                    return True
        return False
