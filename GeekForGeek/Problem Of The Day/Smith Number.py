#User function Template for python3

class Solution:
    def smithNum(self, n):
        def digit_sum(num):
            return sum(int(digit) for digit in str(num))

        prime_factors = {}
        d = n

        for i in range(2, int(d**0.5) + 1):
            while d % i == 0:
                prime_factors[i] = prime_factors.get(i, 0) + 1
                d //= i

        if d == n:
            return 0

        if d > 1:
            prime_factors[d] = prime_factors.get(d, 0) + 1

        sum1 = digit_sum(n)
        sum2 = 0

        for factor, count in prime_factors.items():
            sum2 += count * digit_sum(factor)

        return int(sum1 == sum2)
