#User function Template for python3
class Trie:
    def __init__(self):
        self.root={}
        
    def insert(self, word: str):
        cur=self.root
        for c in word:
            if c not in cur:
                cur[c]={}
            cur=cur[c]
        cur['.']={}

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur:
                return False
            cur=cur[c]
        return '.' in cur

    def isPrefix(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur:
                return False
            cur=cur[c]
        return True
        
