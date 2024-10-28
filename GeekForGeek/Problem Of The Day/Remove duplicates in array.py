class Solution:
    def removeDuplicates(self, arr):
        # code here 
        new_arr=[]
        seen=set()
        for i in arr:
            if i not in seen:
                new_arr.append(i)
                seen.add(i)
                
        return new_arr
        
