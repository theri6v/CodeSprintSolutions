class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)

        
        def is_possible(dist):
            count = 1
            last = arr[0]
            for i in range(1, n):
                if arr[i] - last >= dist:
                    count += 1
                    last = arr[i]
                    if count == k:
                        return True
            return False

        left, right = 0, arr[-1] - arr[0]
        best = 0

        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                best = mid
                left = mid + 1  
            else:
                right = mid - 1 

        return best
