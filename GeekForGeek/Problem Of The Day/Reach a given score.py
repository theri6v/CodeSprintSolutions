#User function Template for python3

class Solution:
    def count(self, n: int) -> int:
       return sum(int((n-i)%5==0)*(1+(n-i)//10) for i in range(0,n+1,3))
        

