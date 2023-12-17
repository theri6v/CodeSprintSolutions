#User function Template for python3
class Solution:
    def findMaxSum(self,arr, n):
        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        incl = arr[0]
        excl = 0

        for i in range(1, n):
            new_excl = max(incl, excl)
            incl = excl + arr[i]  
            excl = new_excl        

        return max(incl, excl)


