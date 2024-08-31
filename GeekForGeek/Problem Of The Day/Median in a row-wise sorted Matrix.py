#User function Template for python3

class Solution:
    def median(self, matrix, R, C):
        
        #code here 
        result=[]
        Mat=matrix
        for ind in Mat:
            result.extend(ind)
     
        result.sort()
        if len(result)%2!=0:
            median=len(result)//2
            return result[median]
        else:
            md1=len(result)//2
            md2=md1-1
            median=result[md1]+result[md2]//2
            return median
