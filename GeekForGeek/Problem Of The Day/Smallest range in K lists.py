import heapq

class Solution:
    def findSmallestRange(self, arr):
        k = len(arr)
        n = len(arr[0])

        # (value, row, index in row)
        min_heap = []
        maxVal = float('-inf')

        # Initialize heap with the first element of each row
        for row in range(k):
            val = arr[row][0]
            heapq.heappush(min_heap, (val, row, 0))
            maxVal = max(maxVal, val)

        # Initialize the smallest range
        start, end = -1e5, 1e5  # Range will always be better than this

        while True:
            minVal, row, idx = heapq.heappop(min_heap)

            # Update result if this range is smaller
            if maxVal - minVal < end - start:
                start, end = minVal, maxVal

            # Move to the next element in the current row
            if idx + 1 == n:
                break  # If any list is exhausted, stop
            nextVal = arr[row][idx + 1]
            heapq.heappush(min_heap, (nextVal, row, idx + 1))
            maxVal = max(maxVal, nextVal)

        return [start, end]
