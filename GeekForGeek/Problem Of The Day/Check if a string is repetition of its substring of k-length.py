from collections import defaultdict

class Solution:
    def kSubstrConcat(self, n, s, k):
        if n % k:
            return 0

        mp = defaultdict(int)
        temp = s[0]

        for i in range(1, n):
            if i % k == 0:
                mp[temp] += 1
                temp = ""
            temp += s[i]

        mp[temp] += 1

        if len(mp) > 2:return 0
        
        count = sum(1 for value in mp.values() if value > 1)
        return 1 if count <= 1 else 0
