#User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        # code here
        found={}
        for item in arr:
            if target-item in found:
                return True
            else:
                found[item]=1
        return False        
