from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        newBoard = []
        n = len(board)
        m = len(board[0])
        newBoard.append(["X" for _ in range(m + 2)])
        for row in board:
            newBoard.append(["X", *row, "X"])
        newBoard.append(["X" for _ in range(m + 2)])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        q = deque([])
        for i in range(1, n  + 1):
            if newBoard[i][1] == "O":
                q.append((i, 1))
            if newBoard[i][m] == "O":
                q.append((i, m))
        
        for j in range(1, m + 1):
            if newBoard[1][j] == "O":
                q.append((1, j))
            if newBoard[n][j] == "O":
                q.append((n, j))
        
        seen = set()
        while q:
            row, col = q.popleft()
            board[row - 1][col - 1] = "2"
            for x, y in directions:
                if newBoard[row + x][col + y] == "O" and (row + x, col + y) not in seen:
                    q.append((row + x, col + y))
            seen.add((row, col))

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "2":
                    board[i][j] = "O"

            