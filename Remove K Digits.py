#User function Template for python3

class Solution:

    def removeKdigits(self, S, K):
        # code here
        stack = []

        for digit in S:
            # Remove digits from the stack as long as the current digit is smaller
            # and there are still digits left to be removed (K > 0)
            while K > 0 and stack and stack[-1] > digit:
                stack.pop()
                K -= 1

            # Push the current digit onto the stack
            stack.append(digit)

        # Remove remaining digits if necessary (K > 0)
        while K > 0:
            stack.pop()
            K -= 1

        # Construct the result string
        result = ''.join(stack).lstrip('0')

        # Return '0' if the result string is empty, else return the result string
        return result if result else '0'

