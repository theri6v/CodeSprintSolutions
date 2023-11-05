#User function Template for python3

class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        # code here
        ans = []
        for t, x, y in queries:
            temp = 0
            if t == 1:
                for i in range(-1,  2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        nx = x + i
                        ny = y + j
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        temp += mat[nx][ny]
                ans.append(temp)
            else:
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        if max(abs(i), abs(j)) != 2:
                            continue
                        nx = x + i
                        ny = y + j
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        temp += mat[nx][ny]
                ans.append(temp)
        
        return ans
