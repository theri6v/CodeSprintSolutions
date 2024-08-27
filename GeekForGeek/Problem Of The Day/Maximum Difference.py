class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        ls = [0] * n  # Array to store left smaller elements
        rs = [0] * n  # Array to store right smaller elements
        
        # Calculate left smaller elements
        stack = []
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            ls[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        
        # Calculate right smaller elements
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            rs[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        
        # Calculate the maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(ls[i] - rs[i]))
        
        return max_diff

