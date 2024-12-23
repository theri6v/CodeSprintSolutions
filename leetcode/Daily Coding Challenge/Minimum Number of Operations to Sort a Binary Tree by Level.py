# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: TreeNode | None) -> int:
        def minSwapsToSort(arr):
            n = len(arr)
            indexed_arr = [(value, index) for index, value in enumerate(arr)]
            indexed_arr.sort()  # Sort by value
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or indexed_arr[i][1] == i:
                    continue
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = indexed_arr[j][1]
                    cycle_size += 1
                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        if not root:
            return 0

        ans = 0
        q = deque([root])

        while q:
            level_vals = []
            for _ in range(len(q)):
                node = q.popleft()
                level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans += minSwapsToSort(level_vals)

        return ans
