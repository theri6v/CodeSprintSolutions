#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        mp = {}
        ans = []

        for i in range(n):
            if arr[i] not in mp:
                mp[arr[i]] = []
            mp[arr[i]].append(i)

        for i in range(n):
            for j in range(i + 1, n):
                num = -(arr[i] + arr[j])
                if num in mp:
                    for index in mp[num]:
                        if index > j:
                            ans.append([i, j, index])

        return ans
