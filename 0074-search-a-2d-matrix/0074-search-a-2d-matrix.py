class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0 
        n = len(matrix[0])
        m = len(matrix)
        r = (m * n) - 1
        while l <= r:
            mid = (l + r) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False