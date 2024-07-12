#User function Template for python3
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        if root is None:
            return False
        target -= root.data
        if root.left is None and root.right is None:
            return target == 0
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)

