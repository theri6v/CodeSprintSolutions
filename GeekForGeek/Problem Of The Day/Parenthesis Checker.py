#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        arr = []
        for p in x:
            if p in "({[":
                arr.append(p)
            elif p == ')' and len(arr) > 0 and arr[-1] == '(':
                    arr.pop()
            elif p == '}' and len(arr) > 0 and arr[-1] == '{':
                    arr.pop()
            elif p == ']' and len(arr) > 0 and arr[-1] == '[':
                    arr.pop()
            else:
                return False
        if len(arr) == 0:
            return True
        else:
            return False
