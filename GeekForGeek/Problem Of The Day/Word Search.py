class Solution:
    def isWordExist(self, mat, word):
        #Code here
        if not mat or not word:
            return False
        n,m = len(mat),len(mat[0])
        
        def dfs(x,y,index):
            if index == len(word):
                return True
            if x < 0 or x >= n or y < 0 or y >= m or mat[x][y] != word[index]:
                return False
                
            temp , mat[x][y] = mat[x][y],"#"
            
            found = (dfs(x+1,y,index+1) or
                     dfs(x-1,y,index+1) or
                     dfs(x,y+1,index+1) or
                     dfs(x,y-1,index+1))
            mat[x][y] = temp
            return found
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False
        
