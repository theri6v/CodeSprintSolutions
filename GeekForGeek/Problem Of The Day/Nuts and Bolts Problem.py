#User function Template for python3
class Solution:

    def matchPairs(self, n, nuts, bolts):
        # Predefined order
        order = ["!", "#", "$", "%", "&", "*", "?", "@", "^"]
        
        # Temporary lists to hold sorted nuts and bolts
        sorted_nuts = []
        sorted_bolts = []
        
        for i in order:
            if i in nuts:
                sorted_nuts.append(i)
            if i in bolts:
                sorted_bolts.append(i)
        
        # Update the original nuts and bolts lists
        for i in range(n):
            nuts[i] = sorted_nuts[i]
            bolts[i] = sorted_bolts[i]
        
                
