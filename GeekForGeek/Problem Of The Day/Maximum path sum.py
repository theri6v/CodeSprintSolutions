#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
import math

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        max_sum = [-math.inf]
        self.pathSum(root, max_sum)
        return max_sum[0]
        
    def pathSum(self, root, max_sum):
        if root is None:
            return 0
        l_sum = max(0, self.pathSum(root.left, max_sum))
        r_sum = max(0, self.pathSum(root.right, max_sum))
        max_sum[0] = max(max_sum[0], root.data + l_sum + r_sum)
        #print(root.data, l_sum, r_sum, max_sum[0])
        return max(l_sum, r_sum) + root.data
