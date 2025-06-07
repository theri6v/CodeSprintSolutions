class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        prefix_sum_map = {0: -1}
        prefix_sum = 0
        max_length = 0

        for i in range(n):
            prefix_sum += a1[i] - a2[i]
            if prefix_sum in prefix_sum_map:
                length = i - prefix_sum_map[prefix_sum]
                max_length = max(max_length, length)
            else:
                prefix_sum_map[prefix_sum] = i

        return max_length 
