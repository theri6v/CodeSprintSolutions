#User function Template for python3

class Solution:
    def search(self, pat, txt):
        start = 0
        res = []
        while True:
            pos = txt.find(pat, start)
            if pos == -1:
                break
            res.append(pos + 1)  # 1-based index
            start = pos + 1
        return res
