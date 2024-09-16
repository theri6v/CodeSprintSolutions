# User function Template for Python3

class Solution:
    def maxLength(self, s):
        stack = [-1]  # Initialize stack with base index
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        
        return max_len
