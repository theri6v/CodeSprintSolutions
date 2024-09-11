from typing import List
import heapq
class Solution:
   def minCost(self, arr: List[int]) -> int:
        pq=[]
        
        for rope in arr:
            heapq.heappush(pq,rope)
            
        total_cost=0
        
        while len(pq)>1:
            rope1=heapq.heappop(pq)
            rope2=heapq.heappop(pq)
            
            cost=rope1+rope2
            
            total_cost=total_cost+cost
            
            heapq.heappush(pq,cost)
        return total_cost  
