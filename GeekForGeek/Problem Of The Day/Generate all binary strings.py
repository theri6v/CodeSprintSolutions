class Solution:
     def binstr(self, n):
          # code here
          maximun_number = (2**n)-1
          res = []
          
          i = 0
          while i<(maximun_number+1):
               input = bin(i)[2:]

               less = n - len(input)
               add = '0'*less
               actual_add = add+input

               res.append(actual_add)

               i += 1
          return res
