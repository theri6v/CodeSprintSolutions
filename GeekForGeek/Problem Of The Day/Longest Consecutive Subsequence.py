 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        if not arr:
            return 0
        ns=set(arr)
        ml=0
        for num in ns:
            if num-1 not in ns:
                cn=num
                cl=1
                while cn+1 in ns:
                    cn+=1
                    cl+=1
                ml=max(ml,cl)
        return ml
