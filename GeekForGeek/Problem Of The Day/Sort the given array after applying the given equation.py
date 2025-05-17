class Solution:
    def sortArray(self, arr, A, B, C):
        def quad(x):
            return A * x * x + B * x + C

        n = len(arr)
        result = [0] * n
        left, right = 0, n - 1
        index = n - 1 if A >= 0 else 0

        while left <= right:
            left_val = quad(arr[left])
            right_val = quad(arr[right])
            if A >= 0:
                if left_val > right_val:
                    result[index] = left_val
                    left += 1
                else:
                    result[index] = right_val
                    right -= 1
                index -= 1
            else:
                if left_val < right_val:
                    result[index] = left_val
                    left += 1
                else:
                    result[index] = right_val
                    right -= 1
                index += 1

        return result
