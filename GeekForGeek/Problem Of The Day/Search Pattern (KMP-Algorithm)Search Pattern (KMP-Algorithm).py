#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        size_p = len(pat)
        size_t = len(txt)
        list1 = []
        
        for i in range(0,size_p-1+size_t):
            s = txt[i:i+size_p]
            if s == pat:
                list1.append(i)
        
        return list1        
