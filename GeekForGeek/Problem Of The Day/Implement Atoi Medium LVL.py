#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Constants for INT_MAX and INT_MIN
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
    
        # Initialize variables
        i = 0
        n = len(s)
        sign = 1
        result = 0
    
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
    
        # Step 2: Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
    
        # Step 3: Read digits and ignore non-digit characters
        while i < n and s[i].isdigit():
            digit = int(s[i])
    
            # Step 4: Check for overflow and clamp the value
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
    
            result = result * 10 + digit
            i += 1
    
        # Return the final result with the appropriate sign
        return sign * result
