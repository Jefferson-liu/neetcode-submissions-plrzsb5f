class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        m = len(matrix[0])
        top, left = False, False
        


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        top = True
                    if j > 0:
                        matrix[0][j] = 0
                    else:
                        left = True

        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0

        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0
        
        if top:
            for j in range(m):
                matrix[0][j] = 0
        if left:
            for i in range(n):
                matrix[i][0] = 0
        
        