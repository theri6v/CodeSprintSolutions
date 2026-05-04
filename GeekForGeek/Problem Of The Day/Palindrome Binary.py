class Solution:
    def isBinaryPalindrome(self, n):
        # Convert integer to binary string
        binary = bin(n)[2:]
        
        # Check palindrome
        if binary == binary[::-1]:
            return 1
        return 0
