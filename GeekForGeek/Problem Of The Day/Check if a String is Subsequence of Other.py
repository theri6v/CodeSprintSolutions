class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        l,r = 0,0
        
        while l < len(s1) and r < len(s2):
            if s1[l] == s2[r]:
                l +=1
                r+=1
            else:
                r +=1
        
        return l == len(s1)
