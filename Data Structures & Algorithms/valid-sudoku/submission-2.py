class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row, then column, then sub boxes

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            seen = set()
            for j in range(cols):
                if board[i][j] in seen:
                    return False
                else:
                    if board[i][j]  != ".":
                        seen.add(board[i][j])
            
        for j in range(cols):
            seen = set()
            for i in range(rows):
                if board[i][j] in seen:
                    return False
                else:
                    if board[i][j]  != ".":
                        seen.add(board[i][j])
        
        # start at each corner
        for row in range(3):
            for col in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[row*3 + i][col * 3 + j] in seen:
                            return False
                        else:
                            if board[row*3 + i][col * 3 + j] != ".":
                                seen.add(board[row*3 + i][col * 3 + j])
        return True