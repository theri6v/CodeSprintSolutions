#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        l=height[0]
        c=1
        for i in range(len(height)):
            if height[i]>l:
                c+=1
                l=height[i]
        return c
        
