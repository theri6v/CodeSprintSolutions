#User function Template for python3


#Function to find the vertical width of a Binary Tree.
def verticalWidth(root):
    # code here
    
    if not root:
        return 0

    min_pos = max_pos = 0  
    def traverse(node, pos):
        nonlocal min_pos, max_pos 
        if not node:
            return
        min_pos = min(min_pos, pos)  
        max_pos = max(max_pos, pos)  
        traverse(node.left, pos - 1)  
        traverse(node.right, pos + 1)  

    traverse(root, 0)  
    return max_pos - min_pos + 1 
        
