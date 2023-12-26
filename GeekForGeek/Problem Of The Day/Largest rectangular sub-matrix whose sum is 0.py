from typing import List


from typing import List


class Solution:
    def kadne(self, v: List[int]) -> tuple:
        sum = 0
        max_sum = -float("inf")
        left = 0
        right = -1

        start = 0
        for i in range(len(v)):
            sum += v[i]
            if sum > max_sum:
                max_sum = sum
                left = start
                right = i

            if sum < 0:
                sum = 0
                start = i + 1

        return left, right

    def sumZeroMatrix(self, a: List[List[int]]) -> List[List[int]]:
        m = len(a)
        n = len(a[0])

        left = right = up = down = 0

        for i in range(n):
            arr = [0] * m

            for j in range(i, n):
                for k in range(m):
                    arr[k] += a[k][j]

                # Apply Kadane's algorithm efficiently using a hashmap
                sum_map = {0: -1}
                l = r = 0
                curr_sum = 0

                for k in range(m):
                    curr_sum += arr[k]

                    if curr_sum in sum_map:
                        if k - sum_map[curr_sum] > r - l:
                            l = sum_map[curr_sum] + 1
                            r = k + 1
                    else:
                        sum_map[curr_sum] = k

                if (j - i + 1) * (r - l) > (right - left) * (down - up):
                    up = l
                    down = r
                    left = i
                    right = j + 1

        result = []
        for i in range(up, down):
            row = []
            for j in range(left, right):
                row.append(a[i][j])
            result.append(row)

        return result
        
