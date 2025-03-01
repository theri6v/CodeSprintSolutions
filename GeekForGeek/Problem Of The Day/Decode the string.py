class Solution:
    def decodedString(self, s):
        # code here
        a=[]
        num=ans=""
        for i in range(len(s)):
            if s[i]=='[':
                a.append(num)
                num=""
                a.append(ans)
                ans=""
            elif s[i]==']':
                curr=a.pop()
                n=int(a.pop())
                while n:
                    if n%2==1:
                        curr+=ans
                    ans+=ans
                    n>>=1
                ans=curr
            elif s[i].isdigit():
                num+=s[i]
            else:
                ans+=s[i]
        return ans
