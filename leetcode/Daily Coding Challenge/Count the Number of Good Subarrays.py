from collections import Counter
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        num_counter = Counter()
        result = current_sum = start_index = 0

        for end_index, num in enumerate(nums):
            current_sum += num_counter[num]
            num_counter[num] += 1

            while current_sum >= k:
                result += len(nums) - end_index
                current_sum -= num_counter[nums[start_index]] - 1
                num_counter[nums[start_index]] -= 1
                start_index += 1

        return result
