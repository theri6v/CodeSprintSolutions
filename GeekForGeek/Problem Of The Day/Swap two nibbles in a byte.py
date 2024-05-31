#User function Template for python3
class Solution:
    def swapNibbles(self, n: int) -> int:
        rn = (n & 0xF0) >> 4  
        ln = (n & 0x0F) << 4  
        return rn | ln
