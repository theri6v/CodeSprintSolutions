#User function Template for python3
from collections import Counter
class Solution:
    def minValue(self, s, k):
        # code here
        # d = dict()
        # arr = [0]*26
        if len(s) == 0:
            return 0
        d = Counter(s)
        arr = []
        for ch, seq in d.items():
            arr.append([seq, ch])
        arr.sort(reverse = True)    
        # print(arr)
        while k:
            arr[0] = [arr[0][0]-1, arr[0][1]]
            arr.sort(reverse = True)
            k-=1
            
        Sum = 0
        for seq, ch in arr:
            Sum += seq**2
            
        return Sum
            
