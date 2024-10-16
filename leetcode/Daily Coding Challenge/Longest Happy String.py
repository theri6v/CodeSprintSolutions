from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        
        if a > 0:
            heappush(max_heap, [-a, 'a'])
        if b > 0:
            heappush(max_heap, [-b, 'b'])
        if c > 0:
            heappush(max_heap, [-c, 'c'])
        
        result = []
        
        while max_heap:
            current = heappop(max_heap)
            
            if len(result) >= 2 and result[-1] == current[1] and result[-2] == current[1]:
                if not max_heap:
                    break
                
                next_char = heappop(max_heap)
                result.append(next_char[1])
                
                if -next_char[0] > 1:
                    next_char[0] += 1
                    heappush(max_heap, next_char)
                
                heappush(max_heap, current)
            else:
                result.append(current[1])
                
                if -current[0] > 1:
                    current[0] += 1
                    heappush(max_heap, current)
        
        return ''.join(result)
