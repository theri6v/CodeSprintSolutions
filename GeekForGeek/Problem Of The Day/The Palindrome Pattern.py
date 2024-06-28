#User function Template for python3

class Solution:
    def pattern (self, arr):
        # code here
        def is_palindrome(s):
            return s == s[::-1]

        row = []
        col = ['' for _ in range(len(arr[0]))]  # Initialize col with empty strings
        
        # Process row-wise
        for i in range(len(arr)):
            s = ""
            for j in range(len(arr[i])):
                s += str(arr[i][j])
                col[j] += str(arr[i][j])  # Append to the appropriate column
            row.append(s)
        
        
        # Check row-wise palindromes
        for i in range(len(row)):
            if is_palindrome(row[i]):
            #   print(i," R")
               return str(i) + " R"
        
        # Check column-wise palindromes
        for j in range(len(col)):
            if is_palindrome(col[j]):
                # print(j," C")
               return str(j) + " C"
        
        return "-1"
                
                

