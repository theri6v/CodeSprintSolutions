class Solution:
    def findNth(self,n):
        result = []
        while n > 0:
            result.append(n % 9)
            n //= 9
        return int(''.join(map(str, result[::-1])))
