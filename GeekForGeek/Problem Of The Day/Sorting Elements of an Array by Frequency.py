#User function Template for python3
from collections import Counter
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        res=[]
        # Create a Counter object
        count = Counter(arr)
        
        # Sort the numbers by frequency (descending) and then by the number value (ascending)
        sorted_numbers = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        
        # Print each number according to its frequency
        for number, freq in sorted_numbers:
            for i in range(freq):
                res.append(number)

        return res
