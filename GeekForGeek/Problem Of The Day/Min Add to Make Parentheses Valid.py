class Solution:
    def minParentheses(self, s):
        o=0
        res=0
        for i in s:
            if i=='(':
                o+=1
            elif o>0:
                o-=1
            else:
                res+=1
        res+=o
        return res
