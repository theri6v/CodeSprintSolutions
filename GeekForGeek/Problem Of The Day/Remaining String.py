#User function Template for python3
class Solution:
    def printString(self, s, ch, count):
        c=0
        for i in range(len(s)):
            if c==count:
                return s[i:]
            if s[i]==ch:
                c+=1
        return ""
