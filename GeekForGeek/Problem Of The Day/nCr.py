import math
class Solution:
    def nCr(self, n, r):
        first=math.factorial(n)
        second=math.factorial(abs(n-r))
        third=math.factorial(r)
        return(first//(second*third))
