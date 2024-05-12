#User function Template for python3

class Solution:
    def minSteps(self, target):
        # code here
        target = abs(target)
        step = total = 0

        while total < target:
            step += 1
            total += step
        
        while (total - target) % 2 != 0:
            step += 1
            total += step

        return step
