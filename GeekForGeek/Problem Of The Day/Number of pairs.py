#User function Template for python3
import bisect

class Solution:
    # Function to count the number of pairs (x, y) such that x^y > y^x
    def countPairs(self, x, y):
        
        # Helper function to find the index of the first element in 'arr' that is greater than 'x'
        def upper_bound(arr, x):
            # bisect_right returns the insertion point which gives the number of elements <= x
            index = bisect.bisect_right(arr, x)
            return index
        
        # Initialize counts for special values
        count_zero = count_one = count_two = count_three = count_four = 0
        
        # Count occurrences of 0, 1, 2, 3, and 4 in array 'y'
        for num in y:
            if num == 0:
                count_zero += 1
            elif num == 1:
                count_one += 1
            elif num == 2:
                count_two += 1
            elif num == 3:
                count_three += 1
            elif num == 4:
                count_four += 1
        
        # Sort the array 'y' to use binary search
        y.sort()
        
        ans = 0
        
        # Iterate over each element 'i' in array 'x'
        for i in x:
            if i == 0:
                # x = 0 does not contribute to any valid pair as 0^y is never greater than y^0 for y > 0
                continue
            elif i == 1:
                # x = 1 is only greater than y^1 if y = 0. Hence, count all zeros in y
                ans += count_zero
                continue
            elif i == 2:
                # For x = 2, calculate how many elements in y are greater than 2
                index = upper_bound(y, i)
                if index != len(y):
                    ans += len(y) - index  # Number of elements in y that are > 2
                # Subtract cases where 2^y is not greater than y^2 (when y = 3 or 4)
                ans -= count_three
                ans -= count_four
                # Add cases where 2^y is greater than y^2 (when y = 0 or 1)
                ans += count_one
                ans += count_zero
            else:
                # For x > 2, calculate how many elements in y are greater than x
                index = upper_bound(y, i)
                if index != len(y):
                    ans += len(y) - index  # Number of elements in y that are > x
                # Add cases where x^y is greater than y^x based on special numbers
                ans += count_one
                ans += count_zero
                # For x = 3, add specific cases for y = 2
                if i == 3:
                    ans += count_two
        
        return ans

