#User function Template for python3
class Solution:

    def checkTriplet(self,arr, n):
        # code here
        squares = [x**2 for x in set(arr)]
        values = dict()
        for v in squares:
            values[v]=True
            
        for i in range(len(squares)):
            for j in range(i+1, len(squares)):
                if squares[i]+squares[j] in values:
                    return True
        return False
        
