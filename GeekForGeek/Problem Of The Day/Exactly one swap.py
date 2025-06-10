class Solution:
    def countStrings(self, s): 
        n=len(s)
        sum=n*(n-1)//2
        freq=[0]*26
        for char in s:
            freq[ord(char)-ord('a')]+=1
        
        count=0
        hasDuplicate=False
        for i in range(26):
            if freq[i]>1:
                count+=(freq[i]*(freq[i]-1))//2
                hasDuplicate=True
        r=sum-count
        return r+1 if hasDuplicate else r
