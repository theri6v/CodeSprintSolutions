
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        even="bdfhjlnprtvxz"
        ans=0
        ss=set(s)
        for i in ss:
            if i in even:
                if s.count(i)%2==0:
                    ans+=1
            else:
                if s.count(i)%2!=0:
                    ans+=1
        if ans%2==0:
            return "EVEN"
        return "ODD"

