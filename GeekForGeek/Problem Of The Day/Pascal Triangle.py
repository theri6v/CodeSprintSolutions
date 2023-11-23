#User function Template for python3

class Solution:

    def nthRowOfPascalTriangle(self,n):
        MOD = 10**9 + 7
        row = [0] * (n)
        row[0] = 1
    
        for i in range(1, n):
            prev = row[0]
            for j in range(1, i + 1):
                temp = row[j]
                row[j] = (prev + row[j]) % MOD
                prev = temp
    
        return row
