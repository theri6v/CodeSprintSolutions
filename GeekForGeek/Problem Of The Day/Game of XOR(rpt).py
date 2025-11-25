class Solution:
    def subarrayXor(self, arr):
        len1 = res = 0
        for i in arr:
            if not len1%2:
                res = res^arr[len1]
            len1+=1
        return res if len1%2 else 0
