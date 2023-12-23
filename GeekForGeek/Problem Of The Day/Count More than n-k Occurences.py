#User function Template for python3


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        dic={}
        for a in arr: dic[a]=dic.get(a,0)+1
        return len([f for f in dic if dic[f]>n/k])
