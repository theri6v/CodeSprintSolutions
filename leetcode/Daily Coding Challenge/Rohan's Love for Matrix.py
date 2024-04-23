#User function Template for python3
class Solution:
    def multiply_matrices(self, A, B):
        MOD = 1000000007
        res = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
        return res

    def power_matrix(self, A, n):
        MOD = 1000000007
        result = [[1, 0], [0, 1]] 
        while n > 0:
            if n % 2 == 1:
                result = self.multiply_matrices(result, A)
            A = self.multiply_matrices(A, A)
            n //= 2
        return result

    def firstElement(self, n):
        if n == 1:
            return 1
        original_matrix = [[1, 1], [1, 0]]
        powered_matrix = self.power_matrix(original_matrix, n)
        return powered_matrix[1][0] % 1000000007
