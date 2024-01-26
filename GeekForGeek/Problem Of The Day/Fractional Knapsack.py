#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        arr.sort(key=lambda item: item.value/item.weight,reverse=True)
        i,ans=0,0
        while i<n and W>=arr[i].weight:
            ans+=arr[i].value
            W-=arr[i].weight
            i+=1
        if i<n:
            ans+=(W/arr[i].weight)*arr[i].value
        return ans
