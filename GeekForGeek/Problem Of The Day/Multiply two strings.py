#User function Template for python3

class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        # return the product string
        if s1=="0" or s2=="0":
            return "0"
        neg=False
        if s1[0]=='-':
            neg=not neg
            s1=s1[1:]
        if s2[0]=='-':
            neg=not neg
            s2=s2[1:]
        prod=[0 for _ in range(len(s1)+len(s2))]
        for i in range(len(s2)-1,-1,-1):
            digit1=int(s2[i])
            carry=0
            for j in range(len(s1)-1,-1,-1):
                digit2=int(s1[j])
                prod[i+j+1]+=digit1*digit2+carry
                carry=prod[i+j+1]//10
                prod[i+j+1]=prod[i+j+1]%10
            nextIdx=i
            while carry:
                prod[nextIdx]+=carry
                carry=prod[nextIdx]//10
                prod[nextIdx]=prod[nextIdx]%10
                nextIdx-=1
            
        res=''.join(str(x) for x in prod)
        zero=0
        while zero<len(res)-1 and res[zero]=='0':
            zero+=1
        res=res[zero:]
        if neg and res!="0":
            res='-'+res
        return res
                
                
                
