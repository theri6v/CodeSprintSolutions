class Solution:
    def maxSubarraySum(self, arr, k):
        res = curr_sum = sum(arr[:k])
        pos = 0
        for i in arr[k:]:
            curr_sum += (arr[k+pos]-arr[pos])
            res = max(res, curr_sum)
            pos+=1
        return res
