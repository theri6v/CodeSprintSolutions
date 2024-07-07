#User function Template for python3
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def Ancestors(self, root, target):
        '''
        :param root: root of the given tree.
        :return: None, print the space separated post ancestors of given target., don't print new line
        '''
        #code here

        def upperlevel(node, ancestors, target):
            if not node:
                return False
            if node.data == target:
                return True
            ancestors.append(node.data)
            if upperlevel(node.left, ancestors, target) or upperlevel(node.right, ancestors, target):
                return True
            ancestors.pop()
            return False
        
        if not root:
            return []
        
        if root.data == target:
            return []
        
        ancestors = []
        found = upperlevel(root, ancestors, target)
        
        if found:
            return ancestors[::-1]
        else:
            return []
