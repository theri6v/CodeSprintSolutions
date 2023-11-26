#User function Template for python3

class Solution:
    def pattern(self, N):
        # code here
        p=N
        li=[]
        while N>0:
            li.append(N)
            N-=5
        while(N<=p):
            li.append(N)
            N+=5
        return li
