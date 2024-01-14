#User function Template for python3

class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        s=set()
        ans=[]
        for i in range(m):
            row=0
            for item in arr[i]:
               row=(row<<1)+item
            if row in s:
               ans.append(i)
            else:
               s.add(row)
        return ans
