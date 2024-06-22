class Solution:
    def ExtractNumber(self,sentence):
        #code here
        words = sentence.split(" ")
        maxi = -1
        
        for word in words:
            if word.isnumeric() and "9" not in word:
                maxi = max(maxi, int(word))
        
        return maxi
