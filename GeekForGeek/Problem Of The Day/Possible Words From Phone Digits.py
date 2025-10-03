class Solution:

    chars={
        2:"abc",
        3:"def",
        4:"ghi",
        5:"jkl",
        6:"mno",
        7:"pqrs",
        8:"tuv",
        9:"wxyz"
    }
    
    def solve(self,arr,i,curr,res):
        if i==len(arr):
            res.append("".join(curr))
            return
        if arr[i] not in Solution.chars:
            self.solve(arr,i+1,curr,res)
            return
        for ch in Solution.chars[arr[i]]:
            curr.append(ch)
            self.solve(arr,i+1,curr,res)
            curr.pop()

    def possibleWords(self, arr):
        n=len(arr)
        res=[]
        self.solve(arr,0,[],res)
        return res
