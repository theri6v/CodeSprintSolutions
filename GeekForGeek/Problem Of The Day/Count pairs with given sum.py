class Solution:
    def countPairs(self,arr, target):
        
        #Your code here
        
        freq = {}
        count = 0
        for num in arr:
            complement = target - num
            if complement in freq:
                count += freq[complement]
            freq[num] = freq.get(num, 0) + 1
        
        return count
