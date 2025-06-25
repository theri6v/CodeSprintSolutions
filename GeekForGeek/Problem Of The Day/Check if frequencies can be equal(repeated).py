class Solution:
    def sameFreq(self, s: str) -> bool:
        def isEqual(freq):
            f = -1
            for count in freq:
                if count:
                    if f == -1:
                        f = count
                    elif f != count:
                        return False
            return True

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        if isEqual(freq):
            return True

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] -= 1
            if isEqual(freq):
                return True
            freq[idx] += 1

        return False
