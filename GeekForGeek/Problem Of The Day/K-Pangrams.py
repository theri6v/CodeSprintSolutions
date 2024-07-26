#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        alphabetSet= set("abcdefghijklmnopqrstuvwxyz")
        distinctCharSet = set(string.replace(" ",""))
        MissingChars= alphabetSet - distinctCharSet
        numberOfMissingChars = len(MissingChars)
        result = ((numberOfMissingChars <= len(string.replace(" ", ""))-len(distinctCharSet)) and (numberOfMissingChars <= k)) 
        return result
