#User function Template for python3

class Solution:
    def canPair(self, nuns, k):
        n = len(nums)
        if n % 2 == 1:
            return False

        freq = [0] * k
        for i in nums:
            curr = i % k
            if freq[(k - curr) % k] != 0:
                freq[(k - curr) % k] -= 1
            else:
                freq[curr] += 1

        for i in freq:
            if i != 0:
                return False

        return True
