import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        n = len(a)
        a.sort(reverse=True)
        b.sort(reverse=True)

        max_heap = [(-(a[0] + b[0]), 0, 0)]
        visited = {(0, 0)}
        result = []

        while len(result) < k:
            neg_sum, i, j = heapq.heappop(max_heap)
            result.append(-neg_sum)

            # Push (i+1, j) if not visited
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))

            # Push (i, j+1) if not visited
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))

        return result
