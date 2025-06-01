class Solution:
    def countPairs(self, mat1, mat2, x ):
        # code here
        n=len(mat1)
        s=set()
        count=0
        for i in range(n):
            for j in range(n):
                s.add(mat2[i][j])
        for i in range(n):
            for j in range(n):
                if x-mat1[i][j] in s:
                    count+=1
        return count
