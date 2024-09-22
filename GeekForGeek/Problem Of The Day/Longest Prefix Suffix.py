#User function Template for python3

class Solution:
    def lps(self, string):
        # code here
        n = len(string)
        lps = [0] * n  
        length = 0    
        i = 1
        while i < n:
            if string[i] == string[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps[-1]
        
