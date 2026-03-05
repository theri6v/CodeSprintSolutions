class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        # 2 pointers Initialized
        start = 0
        end = 0
        
        # Frequency Map
        freq = {}
        
        # Max length variable
        res = -1
        
        # Loop till we reach end
        while start<=end and end <len(s):
            # Add char
            if s[end] not in freq:
                freq[s[end]] = 0
            freq[s[end]] += 1
            
            # if we have sufficient ele calculate length
            if len(freq) == k:
                res = max(res, end-start+1)
                end+=1
            #  if length is > required shrink it and also remove added character
            elif len(freq) > k:
                freq[s[start]] -=1
                if freq[s[start]] <= 0:
                    del freq[s[start]]
                start+=1
                freq[s[end]] -= 1
                if freq[s[end]] <= 0:
                    del freq[s[end]]
            # if length is < than k expand the window 
            else:
                end+=1
        
        # return response
        return res
