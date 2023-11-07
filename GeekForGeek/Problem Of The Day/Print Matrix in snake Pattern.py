#User function Template for python3

class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here
        lst =[]
        for x in matrix:
            if matrix.index(x)%2==1:
               list(map(lst.append,x[::-1]))
            else:
                list(map(lst.append,x))
        
        return lst
