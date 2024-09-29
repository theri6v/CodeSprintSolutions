#User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        cnt=0
        for num in arr:
            rem=num % k
            if int(num/k) >= 0:
                cnt+=int(num/k)
                if rem>0:
                    cnt+=1
        return cnt
