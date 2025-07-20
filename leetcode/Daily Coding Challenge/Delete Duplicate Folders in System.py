from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ans = []
        path = []
        subtree_to_nodes = defaultdict(list)
        
        paths.sort()
        
        root = TrieNode()
        for p in paths:
            node = root
            for s in p:
                node = node.children[s]
        
        self.build_subtree_to_nodes(root, subtree_to_nodes)
        
        for nodes in subtree_to_nodes.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True
    
        self.construct_path(root, path, ans)
        return ans
    
    def build_subtree_to_nodes(self, node: TrieNode, subtree_to_nodes: dict) -> str:
        subtree = "("
        for s, child in node.children.items():
            subtree += s + self.build_subtree_to_nodes(child, subtree_to_nodes)
        subtree += ")"
        if subtree != "()":
            subtree_to_nodes[subtree].append(node)
        return subtree

    def construct_path(self, node: TrieNode, path: List[str], ans: List[List[str]]):
        for s, child in node.children.items():
            if not child.deleted:
                path.append(s)
                self.construct_path(child, path, ans)
                path.pop()
        if path:
            ans.append(path[:])
