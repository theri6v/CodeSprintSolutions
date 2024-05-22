
#User function Template for python3


class Solution:
    def findSmallestMaxDist(self, stations, K):
        # Code here
        def possible(distance):
            station_to_add = 0
            for i in range(len(stations) - 1):
                station_to_add += math.ceil((stations[i + 1] - stations[i]) / distance) - 1
            return station_to_add <= K

        left = 0
        right = stations[-1] - stations[0]
        
        while right - left > 1e-6:
            mid = left + (right - left) / 2.0
            if possible(mid):
                right = mid
            else:
                left = mid
                
        return right