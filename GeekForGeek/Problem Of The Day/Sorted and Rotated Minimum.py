#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        low = 0
        high = len(arr)-1
        ans = float("inf")
        while low<=high:
            mid = (low+high)//2
            if arr[low] <= arr[high]:
                high = mid-1
            else:
                if arr[low] <= arr[mid]:
                    low = mid+1
                else:
                    high = mid -1
            ans = min(ans,arr[mid])
        return ans
