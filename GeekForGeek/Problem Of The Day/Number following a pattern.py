#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob, S):
        # A stack to keep track of the numbers for 'D's
        stack = []
        # A list to keep track of the result
        result = []
        
        for i, ch in enumerate(S):
            if ch == 'I':
                # Append the current number to the result
                result.append(str(i + 1))
                # Append all elements from the stack to the result
                while stack:
                    result.append(str(stack.pop()))
            else: # ch == 'D'
                # Push the current number onto the stack
                stack.append(i + 1)
        
        # Append the last number to handle the last 'D' if there is one
        result.append(str(len(S) + 1))
        # Append all remaining elements from the stack to the result
        while stack:
            result.append(str(stack.pop()))
            
        # Convert the result list to a string and return it
        return ''.join(result)
