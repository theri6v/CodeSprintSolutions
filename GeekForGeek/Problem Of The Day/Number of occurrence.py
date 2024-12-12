class Solution:
    def countFreq(self, arr, target):
        t=0
        for num in arr:
            if num==target:
                t=t+1
        return t
