#User function Template for python3

class Solution:
    def search(self, pattern, text):
        n = len(text)
        m = len(pattern)
        index_arr = []

        for i in range(n):
            if text[i:i+m] == pattern:
                index_arr.append(i + 1)

        return index_arr
