class Solution:
    def solve(self,n,digit,temp,res,k):
        if len(temp)==k:
            if n==0:
                res.append(temp.copy())
            return
        if n<=0 or digit==0:
            return
        temp.append(digit)
        self.solve(n-digit,digit-1,temp,res,k)
        temp.pop()
        self.solve(n,digit-1,temp,res,k)

    def combinationSum(self, n, k):
        res=[]
        self.solve(n,9,[],res,k)
        return res
