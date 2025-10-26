class Solution:
    def minCost(self, arr):
        import heapq
        heapq.heapify(arr)
        tot=0
        for _ in range(len(arr)-1):
            a=heapq.heappop(arr)
            b=arr[0]
            tot+=a+b
            heapq.heapreplace(arr,a+b)
        return tot
