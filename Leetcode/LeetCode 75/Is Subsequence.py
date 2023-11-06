class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, m, n = 0, 0, len(s), len(t)
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m

# follow up
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # pre-processing step
        index = defaultdict(list)
        for i, c in enumerate(t):
            index[c].append(i)
        
        # iterate through each incoming string s
        j = 0
        for c in s:
            if c not in index:
                return False
            pos_list = index[c]
            pos = bisect_left(pos_list, j)
            if pos == len(pos_list):
                return False
            j = pos_list[pos] + 1
        return True
