class Solution:
    def minTime(self, root, target):
        # code here
        def f(root):
            
            if not root:
                return
            if root.data == target:
                t[0] = root
            if root.left:
                d[root.left] = root
                f(root.left)
            if root.right:
                d[root.right] = root
                f(root.right)
        t = [-1]
        d = {}
        f(root)
        vis = set()
        q = [(t[0], 0)]
        vis.add(t[0])
        tt = 0
        while(q):
            node, time = q.pop(0)
            tt = time
            if node.left and node.left not in vis:
                vis.add(node.left)
                q.append((node.left, time + 1))
            if node.right and node.right not in vis:
                vis.add(node.right)
                q.append((node.right, time + 1))
            if node in d and d[node] not in vis:
                vis.add(d[node])
                q.append((d[node], time + 1))
        return tt
