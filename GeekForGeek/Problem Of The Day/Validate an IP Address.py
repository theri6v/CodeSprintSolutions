#User function Template for python3
class Solution:
    def isValid(self, str):
        l = str.split(".")
        if len(l) != 4:
            return False
        for i in l:
            if not i:
                return False
            if i[0] == "0" and len(i) > 1:
                return False
            if i.isdigit() and int(i) in range(0,256):
                pass
            else:
                return False
        return True
