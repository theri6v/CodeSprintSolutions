from functools import reduce
from operator import xor

class Solution:
     def maxSubarrayXOR(self, arr, k):
          # code here
          maxi = curr = reduce(xor, arr[:k])
          pos = 0
          for i in arr[k:]:
               curr ^= i
               curr ^= arr[pos]
               maxi = max(maxi, curr)
               pos += 1

          return maxi
