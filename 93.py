class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check(s):
            if s[0] == '0' and len(s)>1:
                return False
            return 0<=int(s)<=255
        def dfs(idx):
            if len(path)==4:
                res.append('.'.join(path))
                return
            if len(path)==3:
                if check(s[idx:]):
                    path.append(s[idx:])
                    dfs(len(s))
                    path.pop()
                return
            for i in range(max(1, len(s)-idx-3*(3-len(path))), min(3, len(s)-idx-(3-len(path)))+1):
                if check(s[idx:idx+i]):
                    path.append(s[idx:idx+i])
                    dfs(idx+i)
                    path.pop()
        res = []
        path = []
        dfs(0)
        return res
