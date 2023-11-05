class Solution:
    def topK(self, nums, k):
        from collections import Counter
        freq = Counter(nums)
        sorted_elements = sorted(set(nums), key=lambda num: (-freq[num], -num))
        return sorted_elements[:k]
                   
