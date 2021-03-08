class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def check(x, y):
            return 0<=x<=m-1 and 0<=y<=n-1 and not visited[x][y] and grid[x][y] == 1
        def dfs(x, y):
            res = 1
            visited[x][y] = True
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                xx, yy = x+dx, y+dy
                if check(xx, yy):
                    res += dfs(xx, yy)
            return res
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        visited = [[False for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if check(i, j):
                    res = max(res, dfs(i, j))
        return res
