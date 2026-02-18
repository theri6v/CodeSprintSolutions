class Solution:
    def count_and_merge(self, arr, l, m, h):
        n1 = m - l + 1
        n2 = h - m
        left = arr[l:l + n1]
        right = arr[m + 1:m + 1 + n2]
        
        i = 0
        j = 0
        k = l
        res = 0
        
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1
                res += (n1 - i)
        
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
        
        return res

    def count_inversion(self, arr, l, h):
        res = 0
        if h > l:
            m = (l + h) // 2
            res += self.count_inversion(arr, l, m)
            res += self.count_inversion(arr, m + 1, h)
            res += self.count_and_merge(arr, l, m, h)
        return res

    def inversionCount(self, arr):
        N = len(arr)
        return self.count_inversion(arr, 0, N - 1)


