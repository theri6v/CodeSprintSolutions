from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        decrease_count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] < nums[i - 1]:
                decrease_count += 1
                
        return decrease_count <= 1
