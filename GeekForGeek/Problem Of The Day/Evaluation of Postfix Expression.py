import math

class Solution:
    def evaluate(self, arr):
        
        stack = []
        
        for token in arr:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                
                if token == '+':
                    stack.append(val2 + val1)
                elif token == '-':
                    stack.append(val2 - val1)
                elif token == '*':
                    stack.append(val2 * val1)
                elif token == '/':
                    stack.append(math.trunc(val2 / val1))
                    
        return stack.pop()
