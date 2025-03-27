#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        n = len(arr)
        platforms_needed = 0
        result = 0
        i = 0
        j = 0
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms_needed += 1
                i += 1
            else:
                platforms_needed -= 1
                j += 1
            result = max(result, platforms_needed)
        return result 
