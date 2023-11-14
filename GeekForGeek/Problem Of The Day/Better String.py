#User function Template for python3

class Solution:
    def betterString(self, str1, str2):
        def countDistinctSubsequences(s):
            last_occurrence = {}
            dp = [0] * (len(s) + 1)
            dp[0] = 1

            for i in range(1, len(dp)):
                dp[i] = 2 * dp[i - 1]

                if s[i - 1] in last_occurrence:
                    dp[i] -= dp[last_occurrence[s[i - 1]] - 1]

                last_occurrence[s[i - 1]] = i

            return dp[-1]

        count_str1 = countDistinctSubsequences(str1)
        count_str2 = countDistinctSubsequences(str2)
        if count_str1 >= count_str2:
            return str1
        else:
            return str2
        
