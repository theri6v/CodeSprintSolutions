
class Solution:
    def intersectionWithDuplicates(self, a, b):
        # Convert arrays to sets to remove duplicates
        set_a = set(a)
        set_b = set(b)
        
        # Find the intersection of the two sets
        intersection = set_a.intersection(set_b)
        
        # Convert the intersection set back to a list
        result = list(intersection)
        
        return result
        # code here

