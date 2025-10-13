#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self,root):
        def dfs(node):
            if not node:
                return [0,0]
            left = dfs(node.left)
            right = dfs(node.right)
            sum_with_curr = node.data + left[1] + right[1]
            sum_without_curr = max(left) + max(right)
            return [sum_with_curr,sum_without_curr]
        max_sums = dfs(root)
        return max(max_sums)
