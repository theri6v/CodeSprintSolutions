class Solution:
     def generateBinary(self, n):
          # code here
          i = 1
          res = []
          while i<=n:
               res.append(bin(i)[2:])
               i+=1

          return res
