#User function Template for python3
class Solution:
    def NBitBinary(self, n):
        # code here
        res=""
        li=[]
        on=ze=0
        def util(res, on,ze,n):
            if n==0:
                li.append(res)
                return
            if on==ze:
                util(res+"1",on+1,ze,n-1)
            if on>ze:
                util(res+"1",on+1,ze,n-1)
                util(res+"0",on,ze+1,n-1)
        util(res, on,ze,n)
        return li
            
            
        
