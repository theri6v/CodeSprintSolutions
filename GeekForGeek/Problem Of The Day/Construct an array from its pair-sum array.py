class Solution:
    def constructArr(self, arr):
        m = len(arr)
        disc = 1 + 8 * m
        r = int(disc**0.5)
        while (r+1)*(r+1) <= disc:
            r += 1
        while r*r > disc:
            r -= 1
        n = (1 + r) // 2

        if n == 2:
            return [0, arr[0]]
       
        a0 = (arr[0] + arr[1] - arr[n-1]) // 2
        res = [0] * n
        res[0] = a0

        for i in range(1, n):
            res[i] = arr[i-1] - a0

        return res
