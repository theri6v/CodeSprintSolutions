class Solution:
    def cntWays(self, arr):
        arr = [arr[i] if i%2 == 0 else -arr[i] for i in range(len(arr))]
        
        sols = []
        ls = 0
        s = sum(arr)
        for i in range(len(arr)):
            s = s - arr[i]
        
            if  ls - s == 0:
                sols.append(i)
        
            ls = ls + arr[i]
            
        return len(sols)
