class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n-1
        while x <= m-1 and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        return False
