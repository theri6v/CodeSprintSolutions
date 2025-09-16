class Solution:
    def evaluatePostfix(self, arr):
        # code here
        arithmetic = {
            '+' : lambda a, b : a + b,
            '-' : lambda a, b : a - b,
            '*' : lambda a, b : a * b,
            '/' : lambda a, b : a // b,
            '^' : lambda a, b : a ** b
        }

        bucket = []
        for i in arr:
            res = i
            if i in arithmetic:
                arg2 = int(bucket.pop())
                arg1 = int(bucket.pop())
                res = arithmetic[i](arg1, arg2)
            bucket.append(res)

        return bucket[-1]
