class Solution:
    def countConsec(self, n: int) -> int:
        # code here
        # Compute 2^n using bit shifting
        total = 1 << n 

        # Intial 2 values 
        tmp1, tmp2 = 1, 2
        # Compute n_th  terms of Fibonacci
        for i in range(2, n+1):
            tmp1, tmp2 = tmp2, tmp1 + tmp2
        return total - tmp2
