#User function Template for python3
from collections import defaultdict
class Solution:
    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        #code here
        d =defaultdict(list)
        for i in arr:
            s = "".join(sorted(i))
            if s not in d:
                d[s] = [i]
            else:
                d[s].append(i)
        return list(d.values())
