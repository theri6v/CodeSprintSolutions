#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        return ((sum(set(arr))*3)-sum(arr))//2
