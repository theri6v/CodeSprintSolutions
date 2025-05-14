ls =["1"]
for i in range(1,31):
    curr = ls[i-1]
    n = len(curr)
    temp = ""
    j = 0
    while j<len(curr):
        k = j
        while k < len(curr) and curr[k]==curr[j]:
            k+=1
        c = k-j
        temp += str(c)+curr[j]
        j=k
    ls.append(temp)

class Solution:
    def countAndSay(self, n):
        return ls[n-1]
