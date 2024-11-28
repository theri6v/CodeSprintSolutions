#User function Template for python3Asrtyhujikld

class Solution:
    def addBinary(self, s1, s2):
        res=[]
        if len(s1)>len(s2):
            s2n="0"*(len(s1)-len(s2))
            s2n+=s2
            s2=s2n
        elif len(s2)>len(s1):
            s1n="0"*(len(s2)-len(s1))
            s1n+=s1
            s1=s1n
        j=i=len(s1)-1
       # print(s1)
       # print(s2)
        carry=0
        while(i>=0 or j>=0):
            if s1[i]=="1"  and s2[j]=="1":
                num=0+carry
                res.insert(0,str(num))
                carry=1
            elif (s1[i]=="0" and s2[j]=="1") or (s1[i]=="1" and s2[j]=="0"):
                num=1
                if carry==1:
                    num=0
                    res.insert(0,str(num))
                    carry=1
                    
                else:
                    res.insert(0,str(num))
                    carry=0
                    
            else:
                if i==0 and j==0 and carry==0:
                   break
                    
                num=0
                num+=carry
                carry=0
                res.insert(0,str(num))
            i-=1  
            j-=1
        if carry==1:
           res.insert(0,"1")
        ans=""
        for i in range(len(res)):
            if ans=="" and res[i]=="0":
                continue
            else:
                ans+=res[i]
        return ans
    
