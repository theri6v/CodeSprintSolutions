class Solution:

    def findMinDiff(self, arr,M):
        # code here
        n = len(arr)
        arr = sorted(arr)
        left,right = 0,M-1
        ans = float('inf')
        
        while right<n:
            
            max_element = arr[right]
            min_element = arr[left]
            ans = min(ans,max_element-min_element)
            
            left+=1
            right+=1
            
            
        return ans
