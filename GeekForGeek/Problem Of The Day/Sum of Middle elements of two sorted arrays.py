#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        arr = arr1 + arr2
        arr.sort()
        l = len(arr1)
        return arr[l-1] + arr[l]
