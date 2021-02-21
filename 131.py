class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(idx):
            if idx >= n:
                res.append(path[:])
                return
            for i in range(idx, n):
                if dp[idx][i]:
                    path.append(s[idx:i+1])
                    dfs(i+1)
                    path.pop()
        n = len(s)
        dp = [[True for j in range(n)]for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, i-1, -1):
                if i+2 <= j:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j]
        res = []
        path = []
        dfs(0)
        return res
