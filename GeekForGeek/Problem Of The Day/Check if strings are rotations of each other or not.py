#User function Template for python3
class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        
        n = len(s1)
        m = len(s2)
        
        if n!=m:
            return False
      
        s = s1+s1
        if s.count(s2) > 0:
            return 1
        return 0
