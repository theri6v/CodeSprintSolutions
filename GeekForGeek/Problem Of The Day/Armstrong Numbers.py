#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        s=0
        temp=n
        while n>0:
            l=n%10
            n=n//10
            s=s+(l**3)
        if s==temp:
            return "true"
        else:
            return "false"
