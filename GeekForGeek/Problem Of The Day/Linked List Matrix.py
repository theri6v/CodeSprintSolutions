#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Node():
    def __init__(self, value):
        self.data = value
        self.right = None
        self.down = None

class Solution:
    def constructLinkedMatrix(self, grid):
        size = len(grid)
        if size == 0:
            return None

        # Step 1: Create a matrix of Node references
        nodeGrid = [[None for _ in range(size)] for _ in range(size)]
        
        # Step 2: Create Node objects for each element in the grid
        for row in range(size):
            for col in range(size):
                nodeGrid[row][col] = Node(grid[row][col])
        
        # Step 3: Link the nodes together
        for row in range(size):
            for col in range(size):
                if col < size - 1:  # Link to the right
                    nodeGrid[row][col].right = nodeGrid[row][col + 1]
                if row < size - 1:  # Link downwards
                    nodeGrid[row][col].down = nodeGrid[row + 1][col]
        
        # Return the head of the 2D linked list (top-left node)
        return nodeGrid[0][0]
