class Solution:
	def countSubstring(self, s):
		# code here
		freq = [0]*26
		ans = 0
		for c in s:
		    freq[ord(c)-ord('a')] = freq[ord(c)-ord('a')]+1
		    ans += freq[ord(c)-ord('a')]
        return ans
