#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        collect=[]
        for i in range(n):
            collect.append([end[i],start[i],i])
            
        collect.sort()
        end=collect[0][0]
        count=1
        
        for i in range(1,n):
            if collect[i][1]>end:
                end=collect[i][0]
                count+=1
        return count
