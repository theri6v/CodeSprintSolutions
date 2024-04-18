#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        t1=0
        t2=0
        ans=[0]*(n+2)
        for i in arr:
            ans[i]+=1
            if ans[i]==2:
                if t1==0:
                    t1=i
                else:
                    t2=i
                    break
        return [t1,t2]
            
