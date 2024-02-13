#User function Template for python3

'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
'''
import sys
sys.setrecursionlimit(10000)
from collections import deque
class Solution():
    def cloneGraph(self, node):
        visited=dict()
        queue=deque()
        queue.append(node)
        visited[node]=Node(node.val,[])
        while queue:
            u=queue.popleft()
            new_u=visited[u]
            for v in u.neighbors:
                if v not in visited:
                    queue.append(v)
                    visited[v]=Node(v.val,[])
                new_u.neighbors.append(visited[v])
        return visited[node]

