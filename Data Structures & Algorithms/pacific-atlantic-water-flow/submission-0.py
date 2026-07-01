from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        board = []
        n = len(heights)
        m = len(heights[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        board.append([-math.inf for _ in range(m + 2)])
        for row in heights:
            board.append([-math.inf, *[x for x in row], -math.inf])
        board.append([-math.inf for _ in range(m + 2)])
        # pacific is top and left and atlantic is bottom and right
        pq = deque([])
        aq = deque([]) 
        for i in range(1, n + 1):
            pq.append((i, 1))
            aq.append((i, m))
        for j in range(1, m + 1):
            pq.append((1, j))
            aq.append((n, j))

        seenp = set()
        while pq:
            row, col = pq.popleft()
            for x, y in directions:
                if (row + x, col + y) not in seenp:
                    
                    height = board[row + x][col + y]
                    if height >= board[row][col]:
                        pq.append((row + x, col + y))
            seenp.add((row, col))
        

        seena = set()
        while aq:
            row, col = aq.popleft()
            for x, y in directions:
                if (row + x, col + y) not in seena:
                    height = board[row + x][col + y]
                    if height >= board[row][col]:
                        aq.append((row + x, col + y))
            seena.add((row, col))
        
        ans = []
        for seen in seenp:
            if seen in seena:
                ans.append([seen[0] - 1, seen[1] - 1])
        return ans

        