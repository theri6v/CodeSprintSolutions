#User function Template for python3
class Solution:
    def minCandy(self, N, ratings):
        candy = [1]*N
        for i in range(1,N):
            if ratings[i]>ratings[i-1]:
                candy[i] = candy[i-1]+1
                
        for i in range(N-2,-1,-1):
            if ratings[i]>ratings[i+1] and candy[i]<=candy[i+1]:
                candy[i] = candy[i+1]+1
                
        return sum(candy)
