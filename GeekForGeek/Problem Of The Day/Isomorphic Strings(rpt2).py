#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        n1=len(str1)
        n2=len(str2)
        dictn={}
        if n1!=n2:
            return False
        for i in range(n1):
            ch1=str1[i]
            ch2=str2[i]                                                                                
            if not dictn or  (not ch1 in dictn and  not ch2 in dictn.values()):
                     dictn[ch1]=ch2
            else:
                if ch1 in dictn:
                    if dictn.get(ch1)!=ch2:
                        return False
                else:
                    if ch2 in dictn.values():
                        return False
        return True
