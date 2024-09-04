#User function Template for python3

class Solution:
    def nthStair(self,n):
      if n==0:
          return 1
      if n==1:
          return 1
          
      prev2=1
      prev1 =1
      current =1
      
      
      for i in range(2,n+1):
          current =prev2+1
          prev2=prev1
          prev1=current
          
      return current
