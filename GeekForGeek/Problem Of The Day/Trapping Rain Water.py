
class Solution:
    def trappingWater(self, arr, n):
        peaks = []
        for i in range(n):
            if i == 0:
                if arr[i] >= arr[i+1]:
                    peaks.append(i)
                continue
        
            if i == n-1:
                if arr[i] >= arr[i-1]:
                    peaks.append(i)
                continue
            
            if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                peaks.append(i)
        
        # print(peaks)
        l = len(peaks)
        if l <= 1:
            return 0
            
        ans = 0
        start = 0
        while start < l-1:
            nextBiggest = start+1
            for i in range(start+1, l):
                if arr[peaks[i]] >= arr[peaks[start]]:
                    nextBiggest = i
                    break
                
                if arr[peaks[i]] > arr[peaks[nextBiggest]]:
                    nextBiggest = i
            
            # print("nextBiggest: ", nextBiggest)
            
            minn = min( arr[peaks[start]], arr[peaks[nextBiggest]] )
            for i in range(peaks[start], peaks[nextBiggest]+1):
                diff = minn - arr[i]
                if diff > 0:
                    ans += diff
            
            start = nextBiggest
        
        return ans
            
