#User function Template for python3

class Solution:
    def romanToDecimal(self, S):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for i in range(len(S) - 1, -1, -1):
            current_value = roman_values[S[i]]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value

        return result
