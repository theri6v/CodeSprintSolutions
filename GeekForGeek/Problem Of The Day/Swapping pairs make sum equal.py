class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum1=0
        sum2=0
        for i in a:
            sum1+=i
        for i in b:
            sum2+=i
        diff=sum1-sum2
        if (diff%2)!=0:
            return -1
        diff/=2
        e=set()
        for i in a:
            e.add(i)
        for i in b:
            if((i+diff) in e):
                return 1
        return -1
                
                
