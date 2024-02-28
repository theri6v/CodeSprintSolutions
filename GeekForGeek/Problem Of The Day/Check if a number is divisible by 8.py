#User function Template for python3

class Solution:
    def DivisibleByEight(self,s):
        #code here
        s = int(s[-3:])
        if s%8==0:
            return 1
        else:
            return -1
