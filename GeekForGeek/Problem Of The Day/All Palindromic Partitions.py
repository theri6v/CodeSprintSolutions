class Solution:
    def palinParts(self, s):
        def dfs(i, path):
            if i == len(s): return [path]
            res = []
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    res += dfs(j, path+[s[i:j]])
            return res
        return dfs(0, [])
