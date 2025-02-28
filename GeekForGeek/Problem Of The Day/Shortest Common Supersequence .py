class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        len_str1, len_str2 = len(str1), len(str2)
      
        dp_table = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
      
        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                else:
                    dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])
      
        sscs = []
      
        i, j = len_str1, len_str2
      
        while i > 0 or j > 0:
            if i == 0:
                j -= 1
                sscs.append(str2[j])
            elif j == 0:
                i -= 1
                sscs.append(str1[i])
            else:
                if dp_table[i][j] == dp_table[i - 1][j]:
                    i -= 1
                    sscs.append(str1[i])
                elif dp_table[i][j] == dp_table[i][j - 1]:
                    j -= 1
                    sscs.append(str2[j])
                else:
                    i -= 1
                    j -= 1
                    sscs.append(str1[i])
      
        return ''.join(sscs[::-1])
