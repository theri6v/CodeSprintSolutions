#User function Template for python3
from collections import Counter
class Solution:
    def sameFreq(self, s):
        frequency=[0]*26
        for char in s:
            frequency[ord(char)-ord("a")]+=1
        max_val,min_val,max_count,total=0,float("inf"),0,0
        for freq in frequency:
            if freq>0:
                total+=1
                if freq>max_val:
                    max_val=freq
                    max_count=1
                elif freq==max_val:
                    max_count+=1
                if freq<min_val:
                    min_val=freq
        if max_count==total:
            return True
        if max_count==total-1 and min_val==1:
            return True
        if max_count==1 and max_val==min_val+1:
            return True
        return False
