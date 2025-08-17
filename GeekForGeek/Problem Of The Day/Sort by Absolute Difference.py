class Solution:
    def rearrange(self, arr, x):
        arr.sort(key = lambda num : abs(num-x))
        return arr
