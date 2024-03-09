#User function Template for python3

        # code here

class Solution:
    # Function to remove duplicates from a string.
    def removeDuplicates(self, string):
        # Creating a dictionary to store frequency of characters.
        hash_table = {}
        # Declaring a string to store the final answer.
        ans = ""
        # Iterating over every character in the string.
        for c in string:
            # If the character is encountered for the first time,
            # adding it to the answer string and updating its frequency.
            if c not in hash_table:
                ans += c
                hash_table[c] = 1
        # Returning the answer string without duplicates.
        return ans
