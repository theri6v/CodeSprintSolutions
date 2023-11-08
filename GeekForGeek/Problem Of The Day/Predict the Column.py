#User function Template for python3

class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here 
        res = [0] * N

        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    res[j] += 1

        m = max(res)
        return -1 if m == 0 else res.index(m)
