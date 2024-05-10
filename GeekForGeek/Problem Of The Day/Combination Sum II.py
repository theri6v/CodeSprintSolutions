#User function Template for python3

class Solution:
    
     def CombinationSum2(self, arr, n, k):
        # code here
        res=[]
        arr.sort()
        
        def dfs(idx,sumi,path,res):
            if sumi==k:
                res.append(path)
            if sumi>k:
                return 
            for i in range(idx,len(arr)):
                if i>idx and arr[i]==arr[i-1]:
                    continue
                dfs(i+1,sumi+arr[i],path+[arr[i]],res)
        dfs(0,0,[],res)
        return res
