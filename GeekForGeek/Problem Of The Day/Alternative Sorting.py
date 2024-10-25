class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        ar=[]
        arr.sort(reverse=True)
        i=0
        while(i<len(arr)//2):
            ar.append(arr[i])
            ar.append(arr[-i-1])
            i+=1
        if(len(arr)%2==1):
            ar.append(arr[i])
        return ar
