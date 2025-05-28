class Solution:    
    def ValidCorner(self,mat): 
        # Code here 
        m, n = len(mat), len(mat[0])
        for i in range(m):
            row = mat[i]
            
            for j in range(i+1, m):
                cnt = 0
                roww = mat[j]
                for k in range(n):
                    if row[k] == 1 and roww[k] == 1:
                        cnt += 1
                if cnt >= 2:
                    return True
        return False
