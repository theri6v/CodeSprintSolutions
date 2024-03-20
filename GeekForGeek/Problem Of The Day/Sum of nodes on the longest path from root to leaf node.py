#User function Template for python3

class Solution:
    def sumOfLongRootToLeafPath(self,root):
        #code here
        def solve(root, h, currsum):
            if root is None:
                return h,currsum
                
            l, s1 = solve(root.left, h+1, currsum + root.data)
            r, s2 = solve(root.right, h+1, currsum + root.data)
            if l==r:
                if s1>s2:
                    return l,s1
                return r,s2
            if l>r:
                return l,s1
            return r,s2
        return solve(root, 0, 0)[1]
