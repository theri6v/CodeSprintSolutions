class Solution:
    def divby13(self, s):
        # code here 
        r=0
        for d in s:
            r=(r*10+int(d))%13
        return r==0
        
