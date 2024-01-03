#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        N = len(S)
        if "1" not in S or "2" not in S or "0" not in S:
            return -1
        
        def helper(n, s, l):
            for i in range(n):
                if "1" in s[i:i+l] and "2" in s[i:i+l] and "0" in s[i:i+l]:
                    return len(s[i:i+l])
            return helper(n, s, l+1)
        return helper(N, S, 3)
