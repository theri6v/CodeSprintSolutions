#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Complete this function
        if not s:
            return 1
        
        for i in dictionary:
            if s.startswith(i) and self.wordBreak(n,s[len(i):],dictionary):
                return 1
        return 0
