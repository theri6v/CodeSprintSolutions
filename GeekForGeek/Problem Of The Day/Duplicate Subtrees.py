class Solution:

    def helper(self, root, ans, m):
        if not root:
            return "# "

        node = str(root.data) + " "
        node += self.helper(root.left, ans, m)
        node += self.helper(root.right, ans, m)

        if m.get(node, 0) == 1:
            ans.append(root)
        m[node] = m.get(node, 0) + 1

        return node

    def printAllDups(self, root):
        ans = []
        m = {}
        self.helper(root, ans, m)
        return ans
