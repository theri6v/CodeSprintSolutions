#User function Template for python3
class Solution:
    def search(self, pat, txt):
        n = len(txt)
        m = len(pat)
        ans = []

        for i in range(n):
            if txt[i] == pat[0]:
                if txt[i:i+m] == pat:
                    ans.append(i+1)

        return ans

