class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check(x, y):
            return 0<=x<=m-1 and 0<=y<=n-1 and not visited[x][y] and grid[x][y] == '1'
        def dfs(x, y):
            visited[x][y] = True
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                xx, yy = x+dx, y+dy
                if check(xx, yy):
                    dfs(xx, yy)
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)]for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if check(i, j):
                    dfs(i, j)
                    res += 1
        return res
