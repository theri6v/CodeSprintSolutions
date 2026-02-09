class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            # If subarray is already sorted
            if arr[low] <= arr[high]:
                return low
            
            mid = (low + high) // 2
            next_idx = (mid + 1) % n
            prev_idx = (mid - 1 + n) % n
            
            # Check if mid is minimum
            if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
                return mid
            
            # Left part is sorted, go right
            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid - 1
        
        return 0 
