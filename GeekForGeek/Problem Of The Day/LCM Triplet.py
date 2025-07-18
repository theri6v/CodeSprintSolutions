class Solution:
    def lcmTriplets(self,N):
        #code here
        if(N==2):
            return 2
        if N%2==0 and N%3==0 and (N-3)%3==0:
            return (N-1)*(N-2)*(N-3)
        if N%2==0:
            return N*(N-1)*(N-3)
        else:
            return N*(N-1)*(N-2)
