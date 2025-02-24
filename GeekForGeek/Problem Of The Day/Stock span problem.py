
class Solution:
    def calculateSpan(self, arr):
        n1 = len(arr)
        span = [0]*n1
        stack = []
        
        for i in range(n1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
                
            span[i] = i+1 if not stack else i - stack[-1]
            
            stack.append(i)
            
        return span
