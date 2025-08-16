class Solution:
    def findLargest(self, arr):
        arr = list(map(str, arr))
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        result = ''.join(sorted(arr, key=cmp_to_key(compare)))
        return result if result[0] != '0' else "0"
