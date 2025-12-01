class TrieNode:
    def __init__(self):
        self.child = [None, None]
        self.count = 0

class Solution:
    def insert(self, root, num):
        node = root
        for i in range(15, -1, -1):
            bit = (num >> i) & 1
            if not node.child[bit]:
                node.child[bit] = TrieNode()
            node = node.child[bit]
            node.count += 1

    def query(self, root, num, k):
        node = root
        res = 0
        for i in range(15, -1, -1):
            if not node:
                break
            nBit = (num >> i) & 1
            kBit = (k >> i) & 1
            if kBit == 1:
                if node.child[nBit]:
                    res += node.child[nBit].count
                node = node.child[nBit ^ 1]
            else:
                node = node.child[nBit]
        return res

    def cntPairs(self, arr, k):
        root = TrieNode()
        ans = 0
        for num in arr:
            ans += self.query(root, num, k)
            self.insert(root, num)
        return ans
