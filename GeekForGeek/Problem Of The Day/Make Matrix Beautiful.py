class Solution:
    def balanceSums(self, mat):
        # code here
        # first we are determining the max between all sums of all elements for each row 
        # and  all sums of all elemets for each colunm 
        n = len (mat)
        m = len (mat[0])
        sum_rows = list ( )
        sum_colunms = list ( )
        for i in range (0, n):
            r = sum(mat[i])
            sum_rows.append(r)
            
        for j in range (0, m):
            each_colunm = list( )
            for i in range (0, n):   
                c = mat[i][j]
                each_colunm.append(c)  
            sum_colunms.append(sum(each_colunm))    
        mat_sum = max(max(sum_rows), max(sum_colunms))
        
        # now we count the amount of operations  
        operations = list ( )
        for h in sum_rows: 
             o = mat_sum - h
             operations.append (o)
        
        return sum (operations)
