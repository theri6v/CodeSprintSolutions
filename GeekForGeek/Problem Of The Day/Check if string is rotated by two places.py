#User function Template for python3

class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        return (((str2[2:]+str2[:2])==str1) or ((str2[-2:]+str2[:-2])==str1))
