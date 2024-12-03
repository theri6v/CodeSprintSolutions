class Solution:
    def minChar(self, s):
        #Write your code here
        def compute_prefix_function(s: str) -> list:
            n = len(s)
            prefix = [0] * n
            j = 0  # length of previous longest prefix suffix
            for i in range(1, n):
                while j > 0 and s[i] != s[j]:
                    j = prefix[j - 1]
                if s[i] == s[j]:
                    j += 1
                prefix[i] = j
            return prefix
        
        reversed_s = s[::-1]
        combined = s + "$" + reversed_s  # Create a combined string
        
        prefix = compute_prefix_function(combined)
        # The last value in the prefix array tells us the length of the longest palindrome suffix
        longest_palindromic_prefix_len = prefix[-1]
        
        # Minimum number of characters to add to make the string palindrome
        return len(s) - longest_palindromic_prefix_len     
