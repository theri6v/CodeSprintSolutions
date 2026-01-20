class Solution:
    def __init__(self):
        # constructur
        self.last = []
        self.text = []
        
    def append(self, x):
        # append x into document
        self.text.append(x)

    def undo(self):
        # undo last change
        self.last.append(self.text[-1])
        self.text.pop()

    def redo(self):
        # redo changes
        self.text.append(self.last[-1])
        self.last.pop()

    def read(self):
        # read the document
        return "".join(self.text)
