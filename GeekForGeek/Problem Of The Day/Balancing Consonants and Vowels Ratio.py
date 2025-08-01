class Solution:
    def countBalanced(self, arr):
        # code here
        n = len(arr)
        d = {0: 1}
        s = 0
        nums = []
        for i in arr:
            v, c = 0, 0
            for j in i:
                if j in 'aeiou':
                    v += 1
                else:
                    c += 1
            nums.append(v - c)
        cnt = 0
        for i in nums:
            s += i
            rem = s - 0
            if rem in d:
                cnt += d[rem]
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        return cnt
