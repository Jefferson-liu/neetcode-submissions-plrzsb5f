class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(arr, x):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > arr[mid]:
                    left = mid + 1
                elif target < arr[mid]:
                    right = mid - 1
                else:
                    return mid
            return mid 

        vlist = []
        for x in matrix:
            vlist.append(x[0])

        ind = binSearch(vlist, target)
        if matrix[ind][0] > target and ind > 0:
            ind -= 1
        ans = binSearch(matrix[ind], target)
        return matrix[ind][ans] == target