class Solution:
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        def check(mid):
            added = [0] * n
            total_add = 0
            ops = 0
            for i in range(n):
                if i >= w:
                    total_add -= added[i - w]
                effective_height = arr[i] + total_add
                if effective_height < mid:
                    diff = mid - effective_height
                    if ops + diff > k:
                        return False
                    added[i] = diff
                    total_add += diff
                    ops += diff
            return True
        low = min(arr)
        high = low + k
        res = low
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
