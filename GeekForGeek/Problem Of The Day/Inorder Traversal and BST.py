#User function Template for python3
class Solution:
    def isRepresentingBST(self, arr, N):
        last=arr[0]
        for ele in arr[1:]:
            if ele<=last:
                return 0
            last=ele
        return 1
