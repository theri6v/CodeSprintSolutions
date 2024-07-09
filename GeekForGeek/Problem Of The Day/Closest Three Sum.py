#User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest (self, arr, target):
    # Your Code Here
        arr.sort()
        n,ans,minDiff=len(arr),-float("inf"),float("inf")
        for i in range(n-2):
            l,h=i+1,n-1
            while l<h:
                s=arr[i]+arr[l]+arr[h]
                if s==target:
                    return target
                else:
                    currDiff=abs(target-s)
                if currDiff<minDiff:
                    minDiff=currDiff
                    ans=s
                elif currDiff==minDiff and ans<s:
                    ans=s
                if s<target:
                    l+=1
                else:
                    h-=1
        return ans
