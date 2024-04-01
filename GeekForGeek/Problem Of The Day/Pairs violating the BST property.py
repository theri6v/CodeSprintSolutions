
from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
        # code here

class Solution:
    def pairsViolatingBST(self, n : int, root : Optional['Node']) -> int:
        # code here
        def inorder(node, sorted_list):
            if node is None:
                return
            inorder(node.left, sorted_list)
            sorted_list.append(node.data)
            inorder(node.right, sorted_list)
        
        def merge_and_count_inversions(arr, start, mid, end, temp):
            inversions = 0
            i = start
            j = mid + 1
            k = start
            
            while i <= mid and j <= end:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                    inversions += mid - i + 1
                k += 1
            
            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            
            while j <= end:
                temp[k] = arr[j]
                j += 1
                k += 1
            
            for i in range(start, end + 1):
                arr[i] = temp[i]
            
            return inversions
        
        def count_inversions(arr, start, end, temp):
            inversions = 0
            if start < end:
                mid = (start + end) // 2
                inversions += count_inversions(arr, start, mid, temp)
                inversions += count_inversions(arr, mid + 1, end, temp)
                inversions += merge_and_count_inversions(arr, start, mid, end, temp)
            return inversions
        
        sorted_list = []
        inorder(root, sorted_list)
        n = len(sorted_list)
        temp = [0] * n
        inversions = count_inversions(sorted_list, 0, n - 1, temp)
        return inversions       

