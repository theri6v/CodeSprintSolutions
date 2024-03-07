#User function Template for python3

class Solution:
    def longestSubstring(self, s , n):
        # code here 

        max_length = 0
        ans = "-1"
        i = 0
        j = 0
        while i < N and j < N:
            sub_string = S[i:j+1]
            if S.find(sub_string, j+1) != -1:
                length = len(sub_string)
                if length > max_length:
                    ans = sub_string
                    max_length = length
            else:
                i += 1
            j += 1
        return ans
