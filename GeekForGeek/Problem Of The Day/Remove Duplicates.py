#User function Template for python3
class Solution:
    def removeDups(self, str):
        o=[]
        j=list(str)
        for i in j:
            if i not in o:
                o.append(i)
        return "".join(o)
    
