class Solution:
    def strangePrinter(self, string: str) -> int:
        # Length of the input string
        length = len(string)
        # Initialize the operations matrix with infinity, representing the minimum number of turns
        operations = [[float('inf')] * length for _ in range(length)]
      
        # Start from the end of the string and move towards the beginning
        for start in range(length - 1, -1, -1):
            # A single character takes one turn to print
            operations[start][start] = 1
          
            # Fill the operations matrix for substrings [start:end+1]
            for end in range(start + 1, length):
                # If the characters at the start and end are the same,
                # it takes the same number of turns as [start:end-1]
                if string[start] == string[end]:
                    operations[start][end] = operations[start][end - 1]
                else:
                    # If they are different, find the minimum number of turns needed
                    # to print the substring by splitting it at different points (k)
                    for split_point in range(start, end):
                        # The number of turns is the sum of printing both substrings separately
                        operations[start][end] = min(
                            operations[start][end],
                            operations[start][split_point] + operations[split_point + 1][end]
                        )
      
        # Return the minimum number of turns to print the whole string
        return operations[0][-1]
