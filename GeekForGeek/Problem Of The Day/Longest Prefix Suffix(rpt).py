class Solution:
    def getLPSLength(self, s):
        l = len(s)
        i = 0
        j = 1
        while j < l:
            if s[i] == s[j]:
                i += 1
            else:
                j -= i
                i = 0
            j += 1
        return i
