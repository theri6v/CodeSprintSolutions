# Your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isDeadEnd(self, root):
        # Code here
        l=[('N',0)]
        def rec(node) :
            if not node :
                return
            rec(node.left)
            if not node.left and not node.right :
                l.append(('l',node.data))
            else :
                l.append(('N',node.data))
            rec(node.right)
        rec(root)
        for i,x in enumerate(l) :
            if x[0]=='l' :
                if i+1<len(l) and x[1]==l[i-1][1]+1 and x[1]==l[i+1][1]-1 :
                    return True
        return False
