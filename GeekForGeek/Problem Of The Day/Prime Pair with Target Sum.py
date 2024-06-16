
from typing import List


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        nums = [True for _ in range(n + 1)]
        nums[0] = nums[1] = False
        for i in range(2, len(nums)):
            if nums[i] == False:
                continue
            for j in range(i * i, len(nums), i):
                nums[j] = False
        
        for i in range(n + 1):
            if nums[i] and nums[n - i]:
                return [i, n - i]
        
        return [-1, -1]
        

