class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        
        if n == 0:
            return 0
            
        l = [-1] * n
        s = []
        
        for i in range(n):
            c = 0
            while s and arr[s[-1]] < arr[i]:
                s.pop()
            l[i] = s[-1] if s else -1
            s.append(i)
        
        r = [n] * n
        s.clear()
        
        for i in range(n-1, -1, -1):
            c = 0
            while s and arr[s[-1]] < arr[i]:
                s.pop()
            r[i] = s[-1] if s else n
            s.append(i)
            
        a = 0
        
        for i in range(n):
            a = max(a, r[i] - l[i] - 1)
        return a
