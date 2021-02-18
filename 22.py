class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n+1)]
        dp[0].append('')
        for k in range(1, n+1):
            for i in range(k):
                for l in dp[i]:
                    for r in dp[k-i-1]:
                        dp[k].append('('+l+')'+r)
        return dp[-1]
