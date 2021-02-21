class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x, y, node):
            path.append(board[x][y])
            visited[x][y] = True
            node = node[board[x][y]]
            if '#' in node:
                res.add(''.join(path))
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                xx, yy = x + dx, y + dy
                if 0 <= xx <= len(board) - 1 and 0 <= yy <= len(board[0]) - 1 and not visited[xx][yy] and board[xx][yy] in node:
                    dfs(xx, yy, node)
            path.pop()
            visited[x][y] = False
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = True
        res = set()
        path = []
        visited = [[False for j in range(len(board[0]))]for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return list(res)
