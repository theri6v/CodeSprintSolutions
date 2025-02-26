
class Solution:
    def maxOfMins(self, arr):
       # code here
        n = len(arr)
        right = [n]*n
        stk1 = []
       
        for i, x in enumerate(arr):
            while stk1 and arr[stk1[-1]] > x:
                right[stk1.pop()] = i
            stk1.append(i)
        
        left = [-1]*n
        stk2 = []
        for i in range(n-1, -1, -1):
            x = arr[i]
            while len(stk2) and arr[stk2[-1]] > x:
                left[stk2.pop()] = i
            stk2.append(i)
            
        ans = [0]*n
        for i in range(n-1, -1, -1):
            r = right[i]-left[i]-1
            ans[r-1] = max(ans[r-1], arr[i])
            
        for i in range(n-2, -1, -1):
            ans[i] = max(ans[i], ans[i+1])
        
        return ans
               
