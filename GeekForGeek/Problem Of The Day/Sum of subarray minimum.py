class Solution:
    def sumSubMins(self, arr):
        # Code here
        # 09/07/2025 streak
        op=0
        pre=[-1]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                pre[i]=stack[-1]
            stack.append(i)
        #print(pre)
        suf=[len(arr)]*len(arr)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                suf[i]=stack[-1]
            stack.append(i)
        #print(suf)
        # how many elements:
        for i in range(len(arr)):
            val=arr[i]
            p=i-pre[i]
            s=suf[i]-i
            mul=val*(p*s)
            op+=mul
        return op    
