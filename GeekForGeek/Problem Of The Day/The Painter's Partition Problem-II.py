#User function Template for python3

class Solution:
    def minTime (self, arr, n, k):
        low = max(arr)
        high = sum(arr)
        while(low<=high):
            mid = (low+high)//2
            parts = Sumequal(arr,mid)
            if(parts>k):
                low = mid+1
            else:
               high = mid-1
        return low
        
def Sumequal(arr,x):
    n = len(arr)
    cnt = 1
    sumeq = 0
    for i in range(n):
        if sumeq + arr[i] <= x:
            sumeq += arr[i]
        else:
            cnt += 1
            sumeq = arr[i]
    return cnt
    
