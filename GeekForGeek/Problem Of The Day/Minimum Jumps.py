#User function Template for python3
class Solution:
    def minJumps(self, arr):
        #code here
        n = len(arr)
    
        if n == 1:
            return 0
        
        if arr[0] == 0:
            return -1
        
        jumps = 0
        max_reach = arr[0]
        steps = arr[0]
        
        for i in range(1, n):
            if i == n - 1:
                return jumps + 1
            
            max_reach = max(max_reach, i + arr[i])
            
            steps -= 1
            
            if steps == 0:
                jumps += 1
                
                if i >= max_reach:
                    return -1
                
                steps = max_reach - i
        
        return -1
