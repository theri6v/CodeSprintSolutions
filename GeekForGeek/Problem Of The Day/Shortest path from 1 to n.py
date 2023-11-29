#User function Template for python3

class Solution:
    def minimumStep (self, n):
        #complete the function here
        ans=0
        while n>1:
            if n%3==0:
                n=n//3
                ans+=1
            else:
                if n<3:
                    return ans+n-1
                
                ans+=(n%3)
                n=n-(n%3)
                
            # print(ans,n)
        return ans
        
