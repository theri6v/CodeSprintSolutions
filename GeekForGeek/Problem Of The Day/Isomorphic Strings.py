#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        def solve(s1,s2):
            if len(s1)!=len(s2):
                return False
            m={}
            for i in range(len(s1)):
                if s1[i] in m:
                    if m[s1[i]]!=s2[i]:
                        return False
                else:
                    m[s1[i]]=s2[i]
            return True
            
        return solve(str1,str2) and solve(str2,str1)
