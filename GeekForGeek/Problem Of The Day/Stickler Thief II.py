class Solution:
    def maxValue(self, arr):
        # code here
        def rob(arr):
            chosen, notchosen = 0, 0
            for e in arr:
                n_chosen = notchosen + e
                n_notchosen = max(chosen, notchosen)
                chosen, notchosen = n_chosen, n_notchosen
            
            return max(chosen, notchosen)
            
        return max(rob(arr[:-1]), rob(arr[1:]))
