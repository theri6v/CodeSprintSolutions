#User function Template for python3

class Solution:
    def sameOccurrence(self, arr, x, y):
        diffCount = {}  
        diff = 0        
        result = 0

        diffCount[0] = 1

        for i in arr:
            if i == x:
                diff += 1  
            elif i == y:
                diff -= 1  

            result += diffCount.get(diff, 0)

            diffCount[diff] = diffCount.get(diff, 0) + 1

        return result
        # code here
