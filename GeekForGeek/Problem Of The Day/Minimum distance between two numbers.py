class Solution:
    def minDist(self, arr, n, x, y):
        if x not in arr or y not in arr:
            return -1
        
        min_distance = float('inf')
        prev_index = -1
        
        for i in range(n):
            if arr[i]==x or arr[i]==y:
                if prev_index != -1 and arr[i] != arr[prev_index]:
                    min_distance = min(min_distance, i-prev_index)
                prev_index = i
        return min_distance
