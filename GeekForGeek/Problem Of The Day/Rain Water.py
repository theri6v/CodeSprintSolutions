class Solution:
    def maxWater(self, arr):
        n=len(arr)
        lmax=arr[0]
        rmax=arr[-1]
        left=1
        right=n-2
        water=0
        
        while left<=right:
            if lmax<=rmax:
                water+=max(0,lmax-arr[left])
                lmax=max(lmax,arr[left])
                left+=1
            else:
                water+=max(0,rmax-arr[right])
                rmax=max(rmax,arr[right])
                right-=1
                    
        return water
