import heapq

class Solution:
    def catchThieves(self, arr, k):
        cnt = 0
        police = []
        thief = []
        
        for i in range(len(arr)):
            if arr[i] == 'P':
                caught = False
                
                while thief:
                    if thief[0] < i - k:
                        heapq.heappop(thief)
                    elif thief[0] >= i - k:
                        heapq.heappop(thief)
                        caught = True
                        cnt += 1
                        break
                    else:
                        break
                
                if not caught:
                    heapq.heappush(police, i)
            else:
                caught = False
                
                while police:
                    if police[0] < i - k:
                        heapq.heappop(police)
                    elif police[0] >= i - k:
                        heapq.heappop(police)
                        caught = True
                        cnt += 1
                        break
                    else:
                        break
                
                if not caught:
                    heapq.heappush(thief, i)
                
                        
        return cnt
