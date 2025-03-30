class Solution:
    def startStation(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        
        total_gas11=0
        starting_station=0
        
        for i in range(len(gas)):
            total_gas11+=gas[i]-cost[i]
            
            if total_gas11<0:
                total_gas11=0
                starting_station=i+1
            
        if starting_station==len(gas):
            return-1
            
        return starting_station
    
    


