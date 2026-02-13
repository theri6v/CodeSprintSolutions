class Solution:
    
    def digit_sum(self, x):
        s = 0
        while x > 0:
            s += x % 10
            x //= 10
        return s
    
    def getCount(self, n, d):
        left, right = 1, n
        start = -1
        
        # Binary search to find first valid number
        while left <= right:
            mid = (left + right) // 2
            
            if mid - self.digit_sum(mid) >= d:
                start = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if start == -1:
            return 0
        
        return n - start + 1
