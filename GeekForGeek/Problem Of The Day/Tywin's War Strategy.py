class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        count = 0
        half = n // 2
        if n & 1:
            half += 1
            
        ans = []
            
        for num in arr:
            if num % k == 0:
                count += 1
            else:
                x = num % k
                ans.append(k - x)
                
        if count >= half:
            return 0
        else:
            need = 0
            ans.sort()
            for i in range(half - count):
                need += ans[i]
                
            return need
