# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text

from functools import lru_cache

class Solution:
    def wildCard(self,pattern, string):
        @lru_cache(None)
        def dfs(i, j):
            if i == len(pattern) and j == len(string):
                return True
            elif i < len(pattern) and pattern[i: len(pattern)] == "*" * (len(pattern) - i):
                return True
            elif i == len(pattern) and j < len(string):
                return False
            elif i < len(pattern) and j == len(string):
                return False
            elif pattern[i] == "*":
                return dfs(i + 1, j) or dfs(i, j + 1)
            elif (pattern[i] == string[j]) or pattern[i] == "?":
                return dfs(i + 1, j + 1)
            else:
                return False
        return dfs(0, 0)
