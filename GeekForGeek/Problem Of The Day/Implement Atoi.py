#User function template for Python

class Solution:
    def atoi(self, s):
        if not s:
            return -1
        
        sign = 1
        result = 0
        
        if s[0] == '-':
            sign = -1
            s = s[1:]
        
        for char in s:
            if char.isnumeric():
                result = result * 10 + int(char)
            else:
                return -1  
        
        return sign * result
