class Solution:
    def mergeArrays(self, a, b):
        # code here
        ans=a+b
        ans.sort()
        for i in range(len(a)):
            a[i]=ans[i]
        c=len(a)
        for i in range(len(b)):
            b[i]=ans[c]
            c+=1
