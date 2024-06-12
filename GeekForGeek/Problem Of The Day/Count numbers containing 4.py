class Solution:
    def countNumberswith4(self, n : int) -> int:
        e = []
        for i in range(1,n+1): e.append(str(i))

        f = []
        for i in e:
            if '4' in i: f.append(i)

        return len(f)
        
