#User function Template for python3

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        freq = {}
    
    # Count the frequencies
        for char in s:
            freq[char] = freq.get(char, 0) + 1
    
    # Find the first non-repeating character
        for char in s:
            if freq[char] == 1:
                return char
    
    # Return '$' if no non-repeating character is found
        return '$'

    
