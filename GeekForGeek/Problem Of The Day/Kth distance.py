#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        index_dict = {}
        for i, num in enumerate(arr):
            if num in index_dict:
                if i - index_dict[num] <= k:
                    return True
            index_dict[num] = i
        return False
