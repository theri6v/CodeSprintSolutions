class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        mymap={}
        
        for ele in nums:
            if ele not in mymap:
                mymap[ele]=1
            else:
                mymap[ele]+=1
        
        majority=len(nums)//3
        res=[]
        for ele in mymap:
            if mymap[ele]>majority:
                res.append(ele)
        if len(res)>0:
            res.sort()
            return res
        else:
            res.append(-1)
            return res
