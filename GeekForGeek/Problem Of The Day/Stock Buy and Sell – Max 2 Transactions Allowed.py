class Solution:
    def maxProfit(self, prices):
        # code here
        if not prices:
            return 0
        onp = float('inf')
        ofp = 0
        snb = float('inf')
        sfp = 0
        for i in prices:
            onp = min(onp, i)
            ofp = max(ofp, i - onp)
            snb = min(snb, i - ofp)
            sfp = max(sfp, i - snb)
        return sfp
