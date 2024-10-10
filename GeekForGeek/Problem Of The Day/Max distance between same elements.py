class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        index_map = {}

        
        for i, num in enumerate(arr):
            if num not in index_map:
                
                index_map[num] = [i, i]
            else:
                
                index_map[num][1] = i

       
        max_dist = 0
        for indices in index_map.values():
            max_dist = max(max_dist, indices[1] - indices[0])

        return max_dist
