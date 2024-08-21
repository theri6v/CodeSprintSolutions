class Solution:
    def minTime(self, root, target):
        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))
        
        def traverse(node, target):
            if not node:
                return 0
            if node.data == target:
                ret[0] = max(ret[0], maxDepth(node.left))
                ret[0] = max(ret[0], maxDepth(node.right))
                return 1
            
            left = traverse(node.left, target)
            right = traverse(node.right, target)

            if left > 0:
                ret[0] = max(ret[0], left + maxDepth(node.right))
                return left + 1
            
            if right > 0:
                ret[0] = max(ret[0], right + maxDepth(node.left))
                return right + 1

            return 0

        ret = [0]
        traverse(root, target)
        return ret[0]
