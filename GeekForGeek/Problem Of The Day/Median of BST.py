class Solution:
    def inorder(self, root, arr):
        if root is None:
            return
        self.inorder(root.left, arr)
        arr.append(root.data)   
        self.inorder(root.right, arr)
    def findMedian(self, root):
        arr = []
        self.inorder(root, arr)  
        n = len(arr)
        if n == 0:
            return None
        if n % 2 == 0:
            return arr[n//2-1]
        return arr[n//2]
