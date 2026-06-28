import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        # binary search on the ends
        end = [x[-1] for x in matrix]
        row = bisect.bisect_left(end, target)
        if row < n:
            col = bisect.bisect_left(matrix[row], target)
        
            if matrix[row][col] == target:
                return True
        
        return False