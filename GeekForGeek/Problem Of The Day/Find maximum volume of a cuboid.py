#User function Template for python3

class Solution:
    def maxVolume(self, perimeter, area):
        #code here
        l = (perimeter - math.sqrt(perimeter * perimeter - 24 * area)) / 12
        h = (perimeter / 4) - 2 * l
        return l * l * h
