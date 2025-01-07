#User function Template for python3

from collections import Counter
class Solution:
    def countPairs (self, arr, target):
        i, j = 0, len(arr) - 1
        
        ans = 0
        while i < j:
            s = arr[i] + arr[j]
            if s == target:
                if arr[i] == arr[j]:
                    x = j - i + 1
                    ans += ((x * (x - 1)) // 2)
                    break
                
                x, y = 1, 1
                while arr[i] == arr[i + 1]:
                    i += 1
                    x += 1
                while arr[j] == arr[j - 1]:
                    j -= 1
                    y += 1
                ans += x * y
                i += 1
                j -= 1
            elif s < target:
                i += 1
            else:
                j -= 1
        return ans
