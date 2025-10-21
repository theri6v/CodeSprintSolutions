from collections import Counter
class Solution:
	def topKFreq(self, arr, k):
		count = Counter(arr)
		res = []
		for key,value in sorted(count.items(), key=lambda x: (x[1], x[0]), reverse=True):
		    if len(res)==k:
		        break
		    res.append(key)
		    
        return res
