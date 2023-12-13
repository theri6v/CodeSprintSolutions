#User function Template for python3
class Solution:

    def countStrings(self,n):
        # code here
        MOD = 10**9+7
        first =1
        second=2
        lst =[]
        lst.append(first)
        lst.append(second)
        for i in range(2,n+1):
            s = (first + second) % MOD
            lst.append(s)
            first = second
            second = s
        return lst[n] % MOD
