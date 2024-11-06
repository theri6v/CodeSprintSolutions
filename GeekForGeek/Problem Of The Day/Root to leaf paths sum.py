# Your task is to complete this function
# function should return max sum level in the tree
class Solution:
    def treePathSum(self,root):
        # Code here
        def dfs(node,current_sum):
            if not node:
                return 0
            current_sum = 10 * current_sum + node.data
            if not node.left and not node.right:
                return current_sum
            left_sum = dfs(node.left,current_sum)
            right_sum = dfs(node.right,current_sum)
            return left_sum + right_sum
        return dfs(root,0)
