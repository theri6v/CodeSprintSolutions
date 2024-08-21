#User function Template for python3

from typing import List

class Solution:
    def findOrder(self,alien_dict, n, k):
        graph={c:set() for word in alien_dict for c in word}
        
        for i in range(n-1):
            w1,w2=alien_dict[i],alien_dict[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
                
        visited=set()
        res=[]
        
        def toposort(root):
            if root in visited:
                return True
                
            visited.add(root)
            for i in graph[root]:
                toposort(i)
                
            res.append(root)
            return True
            
        for char in graph:
            toposort(char)
            
        return res[::-1]


