#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        s=s.lower()
        arr=[0 for i in range(26)]
        for x in s:
            if(ord(x)-ord("a") in range(0,26)):
                arr[ord(x)-ord("a")]+=1
        # print(arr)
        for x in arr:
            if(x==0):
                return 0
        return 1
