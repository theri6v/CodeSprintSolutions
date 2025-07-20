class Solution:
    def countValid(self, n, arr):
        # code here
        num = '9'
        arr_size = len(arr)

        if n > 1:
            for _ in range(n-1):
                num += '0'
        
        if 0 in arr:
            num = int(num)
            except_first = (10 - arr_size)** n
            res = num - except_first
          
        else:
            num = int(num)
            first = 9 - arr_size
            except_first = (10 - arr_size)**(n - 1)
            res = num - (first * except_first)
          

        return res
